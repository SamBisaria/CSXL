## The News Feed Project
By: Aaron Wang, Sujay Bhilegalkar, Rishi Mantri, Sam Bisaria

### Overview:
Computer Science Organizations across campus are divided into disparate silos, with news split across hard-to-access channels from Slack, Discord, Instagram, GroupMe and innumerable other platforms. Students are often interested in news from all or many of these sources, but may struggle to keep up-to-date. A news feed on the CSXL would aggregate all this information and provide it to students. 

### Key Personas:
- Gary Guest is a member of the public visiting the site, they can only see posts
- Sally Student is a typical student with no permissions besides viewing and comment/reacting to posts.
- Emily Executive is a office/representative of their organization who can do everything Sally Student can do and draft, make, and edit their posts
- Lance Leader is the leader of their organization (or a professor) who can grant 3 users executive permissions on their behalf and can do everything Emily Executive can do
- Ronda Root is the administrator of the website and will be able to post to any channel and mark posts as announcements

### User Stories
- As Gary Guest, I want to be able to view but not comment on posts
- As Sally Student, I want to be able to view the news feed and click on articles so that I can keep up to date with CS activities on campus
- As Sally Student, I want to be able to comment my thoughts on the current/active post I am viewing
- As Sally Student, I want to be able to search for posts and comments
- As Emily Executive I want to be able to draft, edit, and make new posts on behalf of my organization 
- As Emily Executive I should be able to preview my post before I publicize it
- As Emily Executive I should be able to disable comments on my post when I first publicize it
- As Lance Leader, I should be able to assign executives to post on behalf of my organization
- As Ronda Root, I should be able to mark news posts as announcements (pin them)
- As Ronda Root, I should be able to create, edit, delete, and search for posts at will
- As Ronda Root, I should be able to delete comments at will, lock new comments from being posted, and hide all comments on a post

### Wireframes / Mockups: 
Include rough wireframes of your feature’s user interfaces for the most critical user stories, along with brief descriptions of what is going on. These can be hand-drawn, made in PowerPoint/KeyNote, or created with a tool like Figma. To see an example of a detailed wireframe Kris made this summer before building the drop-in feature, see this Figma board. You will notice the final implementation is not 1:1 with the original wireframe!


Individuals can see all the list of all the news articles that have been published. 
![image](https://github.com/comp423-24s/csxl-final-team-c4/assets/93228261/c6d65e96-186d-4fdd-8775-9bd15d62e9a2)


They can click on an individual news article and see it in full length. Comments are at the bottom and Sally student can make a comment. 
![image](https://github.com/comp423-24s/csxl-final-team-c4/assets/93228261/b3569986-9426-4f11-a8ad-570794f9a230)

This is the form to create news articles.
![image](https://github.com/comp423-24s/csxl-final-team-c4/assets/93228261/cd967676-1cce-47ca-97ec-aa3128f8f9b3)


### Technical Implementation Opportunities and Planning
- #### Models:
  - Post:
    1. ID (primary key)
    2. Headline 
    3. Synopsis (Optional pending email)
    4. Main Story (written in Markdown)
    5. Author (relationship to a user)
    6. Organization (optional relationship to an Organization)
    7. State (Draft, Published, Archived)
    8. Slug (unique string used in URL rather than news ID)
    9. Image URL (optional link to an image for use in feed listing)
    10. Publish Date 
    11. Modification Date
    12. Announcement (Yes/No)
    13. Category (Optional)
    14. Upvote Object
  - Post View Page: 
    1. Post
    2. Comment
  - Comment:
    1. Parent Comment  
    2. List of Child Comments
    3. Upvote Count
    4. Downvote Count
    5. List of users who already voted on a post and if it was upvote/downvote
  - Post Draft Page
    1. Post
    2. Organization
  - News Feed Page
    1. List of Posts
- #### Components
  - Upvote/Down vote Model and Component:
    1. Component has simple up and down buttons to rate a post. Stored as likes/dislikes count in the model and displays their sum
    2. Component has a hard floor of 0 likes. Impossible to display < 0 no matter how many dislikes there are stored in the model
    3. Component will not load if user has showUpvote setting to false in their profile 
  - PostViewComponent
    1. contains the Markdown text of the post, title/subject line, and a root/head comment object
  - PostDraftPage
    1. Only subcomponent is  PageViewComponent
    2. Rest of UI is more or less monolithic, with all the features for  editing/making a post
  - NewsFeedComponent:
    1. contains list of PageViewComponents displayed in Ngfor iterations obtained from a service

- #### Routes
  - /news -> News Feed Page
  - /news/slug -> Post View Page

- ### Security and Privacy
  - Only root user and leader + executives for an organization should be able to access drafts for a post
  - Users should only be able to upvote/downvote once
  - Make sure each user's permissions are explicitly limited to what is described in previous sections

