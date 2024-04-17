### Timeline/resource planning

## Execution Roadmap

The MVP development is planned to be executed over a 14-week time period. This includes setup, development, testing, rollout, and feature iteration to find product-market fit. We envision several intermediate milestones that will help us assess our progress with a team of 4 people, 1 frontend developer, 1 backend+DevOps, 1 UI/UX Designer (part-time), and 1 software tester (part-time).

#### Milestone 1

Design Completion and Technical Setup

- Documentation of EPFL APIs, request-response parameters
- UI elements that can serve as building blocks for plugins: dropdowns, filters, buttons, menu bars, cards, etc.
  - This list depends on parameters and support on the APIs
- Figma mockups and user flow documents
- Tequila registration and integration
- Tests to populate UI elements with EPFL-like data
- Tests to check EPFL API status

| **Sprint/Week Number** | **Objective** | **Outcomes** |
| --- | --- | --- |
| Week 1 | Kickoff and Documentation | EPFL API Investigation, Documentation and Scraping prototype scripts; set up project tools, and establish MVP scope. |
| Week 2 | Design and Technical Setup | Initial wireframes, and user flows created, started UI mockups with UI elements for plugins. Configure Tequila Auth. |
| Week 3 | Design Finalization & Application Skeleton | Finalized UI/UX designs, set up development environments, and backend APIs to populate simple UI elements. |

#### Milestone 2

Core Feature Development

- With appropriate EPFL mock integration already in place, quickly prototype features each week
- Test on several devices; revisit design - aspect ratio, feel on different screen sizes and devices

| **Sprint/Week Number** | **Objective** | **Outcomes** |
| --- | --- | --- |
| Week 4 | Food and News Feature Development | Developed two end-to-end features - Food menu, and news, along with basic frontend-backend integration, began unit testing. |
| Week 5 | Printing Service Development & TestingCron Job Automation | Completed Printing Services feature, continued integration and unit testing - supporting several file types, testing on real printers across campus. Setup appropriate cron jobs to cache food and news data. |
| Week 6 | Moodle Development & Testing | Develop Moodle Integration features, integrated all features in frontend, internal testing. |
| Week 7 | Unit and Integration Testing | Write all remaining unit tests, check frontend-backend integration with Integration tests. |

#### Milestone 3

Internal Testing and Pre-Launch Preparation

- Run end-to-end tests for several devices
- Do stress testing for peak load projections, avg load, and run API latency numbers
- Set up appropriate error handling and sentry logging for API failures
- Set up Google Analytics to track user events, setup analytics dashboard, and ensure correct tracking behavior.
- Firebase FCM for notifications

| **Sprint/Week Number** | **Objective** | **Outcomes** |
| --- | --- | --- |
| Week 8 | Internal Testing & Analytics/Monitoring pipelines | Thorough internal testing, load testing, feedback collection, bug fixing, performance testing |
| Week 9 | Pre-Launch Preparations | Final bug fixes and optimizations, prepared app store and launch materials. |

#### Milestone 4

Initial Rollout and Feature Iterations for PMF

- Rollout app to alpha testers

| **Sprint/Week Number** | **Objective** | **Outcomes** |
| --- | --- | --- |
| Weeks 10-11 | Initial Rollout / Alpha Testing | Deployed app to production, monitored app performance, and gathered user analytics/insights and feedback. Active hotfixes as needed. |
| Week 12 | Feature Iteration 1 | Identifying drop-off points, optimizing user experience, rollout updates, improving UI, possibly |
| Week 13 | Beta Testing | Initiate marketing, getting users on the app, promptly addressing feedback to gain trust |
| Week 14 | Full Rollout | Press marketing pedals, offering incentives to join the app - free meals to lucky winners, |

## Development Resources

The primary cost of development of the product comes from developer cost. We estimate the need to secure 4 months of cash for a 4-person team to meet planned and unplanned scenarios. Realistically, this project would need two full-time developers (one on frontend, one on backend+devops), along with two part time contractors for UI design and Testing. We expect the contractors to contribute a total of 2 person-months each, over the 4-month development + GTM timeframe.
 We overprovision cash for a total of 4 person-months to meet unexpected deviations from our envisioned roadmap.

| **Function** | **Required person-months** |
| --- | --- |
| Frontend Android Developer | 4 |
| Backend Java Developer | 4 |
| UI/UX Designer | 2 |
| Software Tester | 2 |
| Surplus Cash Reserves | 4 |

## Deployment Resources

We will need upfront capital for the purchase of 2 MacMini so that one can serve as a redundant replica in case of hardware failures. We will have to purchase a paid plan on Sentry since we will be generating huge amounts of traffic and will need appropriate performance monitoring.

| **Item** | **Cost / unit** | **Units** | **Totals** |
| --- | --- | --- | --- |
| MacMini | 500 CHF | 2 | 1000 CHF |
| UPS | 500 CHF | 1 | 500 CHF |
| Sentry Pro | 100 CHF / month | 4 | 400 CHF |
| Firebase | Free Tier | - | 0 |
| Google Analytics | Free Tier | - | 0 |
| TOTAL | 1900 CHF |

## Maintenance and Upkeep

We will need to constantly monitor services since unexpected changes to APIs can cause temporary downtime. Moreover, as EPFL services evolve, we will need to constantly update our database schema as well and perform relevant database migrations.

Assuming we land EPFL as a customer by the end of our 4 month timeline, the only cost of maintenance is the cost of developers.