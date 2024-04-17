### Design and Implementation

## Frontend

#### Implementation framework

The app will be developed in Java, optimized for Android, and will use the Model-View-ViewModel (MVVM) architecture. This approach will ensure a structured and efficient management of the app's UI and business logic.

#### Dynamic UI Rendering Strategy

The data layer will fetch UI descriptions in a machine-readable format for each feature, such as food menus, Moodle, and printing services, etc. These descriptions will contain details about what frontend fragments that need to be rendered for each plugin.

The ViewModel will interpret these descriptions to determine the fragments to be displayed in the view of each activity. This dynamic rendering will allow for flexible UI adjustments in response to changes in service APIs or UX improvements.

#### Adaptability to Service API Changes

The flexible UI design will be key in adapting to any future API changes. For example, if Moodle adds new sections, these changes will be incorporated in the backend's machine-readable UI description and seamlessly integrated into the app without major redevelopment.

#### Security and Data Management Focus

The frontend will securely store refresh tokens and cache necessary app data. This approach will prioritize the security of sensitive information and the efficiency of the app's performance.

#### Backend Communication via Apache Thrift

The app will have a thrift client built over Android's Httpcore, that can make RPC calls to our backend server. The thrift client is going to leverage Apache Thrift for data serialization and Android's AsyncTask for dispatching requests. This will ensure efficient and reliable communication between the frontend and the backend.

## Authentication

### Tequila OAuth2.0[^1]

The integration of EPFL's Tequila Authentication system within the PocketCampus app is crucial to adoption and success of the MVP. This is primarily for two reasons:

1. EPFL services that are part of the MVP's scope are resources protected by EPFL authentication.
2. Interfacing with Tequila increases legitimacy of the application in the end users' minds. This improves user retention since trust is important for repeated engagement from end-users.


Tequila implements the OAuth2.0 workflow that enables third-party applications to authenticate and authorize EPFL users. The MVP must implement the following workflow to enable access to EPFL-protected resources. Care must be taken to avoid any potential leak of user's private information, even in the event of a data breach.

#### Frontend (Android Application)

1. Initiate Authentication:
 The Android app initiates the OAuth flow by opening a WebView or using a browser intent to navigate to the Tequila authorization URL with the necessary query parameters (`response_type=code`, `client_id`, `redirect_uri`).
2. User Login and Authorization:
 The user logs in using their EPFL credentials and authorizes the PocketCampus app. This step is handled entirely by Tequila's authorization server, ensuring that the user's credentials are not exposed to us.
3. Receive Authorization Code:
 Upon successful authorization, Tequila redirects to the specified `redirect_uri` with an authorization code. The Android app captures this redirect and extracts the authorization code. This code has a single-use validity.
4. Send Code to Backend:
 Instead of sending a request to Tequila and exchanging the authorization code for an access token directly from the Android app, we securely send the code to our backend server. This is crucial for keeping the `client_secret` secure.

#### Backend (Server Application)

1. Receive Authorization Code:
 The backend server receives the authorization code from the Android app.
2. Exchange Code for Token:
 The server makes a POST request to Tequila's token endpoint with the authorization code, `client_id`, `client_secret`, and `redirect_uri` to exchange it for an access token and a refresh token.
3. Receive and Store Tokens:
 On receiving the access and refresh token, we are careful to store neither on the server, and return them to the app client. The access token acts like a session JWT that can be used to make requests to Tequila's resource server on behalf of the user only for a short amount of time, ensuring that our backend cannot imitate the user.
4. API Requests:
 Our Android app makes API requests to the PocketCampus backend server, along with the access token in the request headers. The token's validity is checked on the backend (since it is a JWT), and if valid, it is used to retrieve information from any EPFL service protected by Tequila authentication.
5. Token Refresh:
 If the access token has expired, the validation check fails, and an INITAIATE\_REFRESH response is sent back to the client app. This triggers a refresh flow where the client resends the refresh token to our server that uses the refresh token and client secret to obtain a new access token.

#### Security Considerations

- HTTPS: We must ensure all communications between the Android app, the server, and Tequila's servers are over HTTPS.
- Client Secret: the `client_secret` must not be exposed in the Android application. It should only be used on the server.
- Token Storage: Store access and refresh tokens securely on the client. Consider encryption and secure storage practices such as Android Keystore.
- Redirect URI Handling: Ensure that the custom URI scheme used for the redirect URI is unique to our app to prevent interception by malicious apps.

![](./assets/auth-flow.png)

### Moodle Auth

Since moodle has its own authentication system, we swap the Authorization Code obtained in step 2 for a moodle token and store it on the client device like the refresh token. This token works similar to a refresh+access token with long expiry, which is why we do not store it on the backend.

## Backend

#### Application Logic

The backend server will host all necessary application logic, enabling the client application to access and consume data from EPFL services.

It will handle communications with various EPFL services and fetch data as per user requests.

#### Framework

The backend is developed as a monolithic Java application in Jetty, providing a stable and efficient web server environment. Moreover, we will create replicas of the Jetty container for load balancing.

#### Dynamic View Rendering

The backend will determine changes in the frontend's rendered view based on API responses from EPFL services, like sending an additional card during course evaluations. It will implement APIs to fetch and manage the list of frontend plugins, complete with rendering metadata and associated callbacks for the Android client app.

#### Data Scraping

Based on each service's functional requirements, cron jobs will regularly update data, ensuring the app constantly has access to the latest information, like updated food menus and new news items. Additionally, these recurrent tasks persist success/failure and other relevant statistics in the database so that we are able to track history and status across failures and app restarts.

#### Frontend Plugin Support

For each frontend plugin, tailored backend APIs will be implemented.

For example, the API for the printing service will handle requests for the latest print & finishing options and configurations, while the Moodle plugin API will manage different kinds of filters and course data retrieval.

#### Responsive Backend-Frontend Interaction

The backend will ensure a responsive interaction with the frontend, updating UI elements as necessary based on current data and user interactions, and act on registered notifications as needed. For example, for the camipro service, the app can run periodic queries to fetch camipro updates and reflect them directly on the frontend. Additionally, if the user enables "low balance" notification, the app can fire an RPC call to the backend that will then submit a notification to the FCM queue which the app will then receive and show to the user. In effect, app can itself trigger an API endpoint on our server to "pull"[^2] a notification.

## Data model

We will use MySQL for the database. Non-user-identifying information with high request volumes, such as food menus, will be cached to improve response times. In terms of user data, we are committed to privacy; thus, we will store only non-identifiable information. We document details of the schemas needed below. The exact schema will be decided when we begin the MVP implementation.

### Authless Data

#### FoodMenu

Purpose - Contains information about the daily food menus.

Fields - MenuID (Primary Key), Date, MealType, DishName, Ingredients, NutritionalInfo, Allergens, Price.

Notes - Aimed at providing quick and anonymous access to daily dining options.

#### News

Purpose - Contains information about the news articles published by EPFL.

Fields - NewsID (Primary Key), Date, Headline, ImageURL, originURL, content

Notes - Aimed at providing access to the latest news from EPFL research.

#### CronTab

Purpose - To keep track of the status of scheduled scraping and caching tasks

Fields - UUID (Primary Key), Target = (Food/News/..), Datetime, Status, CurlRequest

Notes - Every time a cron is successful, we add new entries for the next cron. On failure, we need to investigate and restart the automated process manually.

### Auth UserData

#### UserProfile

Purpose - Manages user-specific data with a focus on privacy.

Fields - UserUUID (Primary Key, hashed value of EPFL SCIPER number), CourseList (list of enrolled courses)

Notes - The UserUUID is a hashed value ensuring that individual users cannot be directly identified. The CourseList associated with each user is stored without any personally identifying information.

#### NotificationTasks

Purpose - Manages user's FCM device\_token and

Fields - UUID (Primary Key, not linked to a user), UserUUID (Foreign key, to be able to map which (anonymous) user registers notifications), DeviceToken (FCM device token)

#### InMemory Data

Here we list all the data that stay within the memory of an API call's execution OR the app's data layer. These are still important to standardize because they form the request-response structure that we will have to specify in Apache Thrift.

Printers. For printing service, our API receives the print & finishing options that a user specifies, along with the actual file to print before creating and submitting the job to EPFL print queue

Campiro. This is requested by the app and the response is returned to the app for display without storing transactions or balances on the backend database. We fetch and transmit transaction lists and balance.

Moodle. This is also requested by the app and the request is directly routed to Moodle APIs. Our backend only serves as an intermediary for data-model massaging in case the Moodle APIs change.

## Infrastructure and Deployment

The backend server will be hosted behind an Apache web server that will serve as a reverse-proxy to either our backend server or directly to one of the EPFL websites in case needed. It will also load-balance between several backend replicas that are each running in a Jetty container.

We will host the server on a Mac mini plugged into the EPFL network. This lets us avoid connecting our server to the EPFL VPN - which will inevitably slow down the app. All printing jobs are submitted to EPFL's print queue (hosted by the myPrint service) directly from within EPFL's network.

## Test Plan

#### Plugin Tests

Since we have a dynamic frontend client that can change views, we should test frontend rendering for all plugins we can compose and support.

#### API Integration Tests

We will need to write several tests that routinely check whether our implemented integration to EPFL APIs are working or not. This is crucial both while rolling out new changes and for monitoring changes to these services so that we can be proactive instead of reactive to failures.

#### Performance Testing

We should stress test the app based on projected peak traffic during different times of the day/week/semester. For example, around lunch hours, when everyone is looking for the food menu, we should expect near full MAU as concurrent requests.

We should measure API latency and try to keep it sub-1s because that is the point beyond which users start to notice it.


[^1]: Standards-based single-sign-on were not maturely deployed at EPFL a decade ago. The description is simplified here for clarity, and assumes the infrastructure available at EPFL in 2023.

[^2]: Pull notifications, popularized by Whatsapp, is a way for a client app to initiate a sendNotification to itself. This is in contrast to a push notification where the backend decides to send a notification based on some condition.