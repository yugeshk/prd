# Overview

PocketCampus is an all-in-one mobile application to enhance the university experience for EPFL students. It centralizes various aspects of campus life, from academic schedules to dining options, transportation, and campus events. The app aims to streamline day-to-day activities, making campus studies and life on campus more efficient and interactive.

The app is extensible to support the all-in-one model. New services can be added easily into the app over time. The services fall into two broad categories: (1) those that do not require any authentication and provide convenient access to EPFL information directly on the phone, and (2) those that require authentication, and for which PocketCampus acts as a trusted mediator of the personalized information to deliver to the phone. All authenticated services are enabled via the EPFL single sign-on service (SSO).

The app is free for all students, who are the primary persona for this app. Perhaps later, other personas will be added as additional targets (e.g., professors, or laboratory assistants).

Pragmatically, we plan to develop this app ourselves, with minimal technological dependencies on EPFL's IT infrastructure (other than OAuth2 for single sign-on, which has been agreed upon).

The goal of the MVP is to build a minimal viable app that achieves significant penetration within the EPFL student body, in terms of aggregate downloads, monthly active users, and number of users that have trusted the application with their EPFL SSO credentials.

Based on informal conversations with EPFL management, we plan to reach with this MVP a user threshold that will make the app "_interesting_" to EPFL, so that we can enter into a first commercial contact.

Our model is to operate PocketCampus as a "mobile software-as-a-service" with support for both Android and iOS.

# History

The proof-of-concept (POC) built during the semester had only basic features (Food, People directory, Public transit schedule). This included a mix of authenticated and unauthenticated features that demonstrates usefulness of the app.

The implementation of the PoC is totally hardwired; each feature consists of a different module within the Android application. For a solution like PocketCampus to be successful, we need to rethink the product and design it with extensibility in mind. Therefore, the MVP requires a change in the architecture.