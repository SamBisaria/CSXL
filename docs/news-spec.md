## The News Feed Project
By: Aaron Wang, Rishi Mantri, Sujay Bhilegalkar, Sam Bisaria

### Overview:
Computer Science Organizations across campus are divided into disparate silos, with news split across hard-to-access channels from Slack, Discord, Instagram, GroupMe and innumerable other platforms. Students are often interested in news from all or many of these sources, but may struggle to keep up-to-date. A news feed on the CSXL would aggregate all this information and provide it to students. 

We made a news page where students can view posts made by those given permissions, such as professors or club leaders. These people have the ability to create drafts, alter or delete those drafts, create posts, and edit their own posts. Some have access to make announcements. The administrator has the ability to do all of that, and alter and delete posts/announcements that belong to other people. 

Can be run locally according to instructions in get_started.md

### Viewing Posts:
The posts can be seen on the main news page on the csxl, the code for which is at csxl-final-team-c4/frontend/src/app/news/post-page while the "News Drafts" page contains only drafts made by the specific author, and the code for this is located at csxl-final-team-c4/frontend/src/app/news/news-view-drafts. Both of these rely on the widget app-view-post which is in news/widgets/view-post, which is given a post or draft as an input. Both of these work by getting the data from a map in the news/news.service.ts, the frontend service, which can either be the map containing drafts or posts. The service gets its info from the backend APIs, for viewing it is specifically the GET requests, and the API requests get or send info to the backend services. The APIs are at backend/api/news.py and the backend service is at backend/services/news.py. These mainly rely on PostModel at backend/models/news_post.py, and the entities PostEntity and UserEntity at backend/entities/post_entity.py and backend/entities/user_entity.py respectively. 

### Creating Posts:
The posts can be made by pressing the create button on the News Drafts page of the CSXL website, which routes to the newsform page, which is at frontend/src/app/news/news-create-post. This form allows one to make the title, synopsis, main body, and to make it an announcment (if the user is allowed). This uses services in news/news.service.ts, which sends a POST request using the backend APIs in backend/api/news.py which use the services at the backend service in backend/services/news.py. These mainly rely on PostModel at backend/models/news_post.py, and the entities PostEntity and UserEntity at backend/entities/post_entity.py and backend/entities/user_entity.py respectively. 

### Editing/Deleting Posts:
The posts can be edited or deleting by pressing icons on the individual posts or drafts on the main News page or the News Drafts page. The editing uses the same form as creating posts, which is at frontend/src/app/news/news-create-post. This form allows one to edit the title, synopsis, main body, and to make it an announcment (if the user is allowed). This uses services in news/news.service.ts, which can send PUT or DELETE requests using the backend APIs in backend/api/news.py which use the services at the backend service in backend/services/news.py. These mainly rely on PostModel at backend/models/news_post.py, and the entities PostEntity and UserEntity at backend/entities/post_entity.py and backend/entities/user_entity.py respectively. 
