export interface Post {
  id: number | null;
  headline: string;
  synopsis?: string; // Optional
  main_story: string;
  author: number; // Change type to user
  slug: string;
  state: String; // Boolean type thing? Draft, Published.
  image_url?: string;
  publish_date: String;
  mod_date: String;
  announcement: boolean; // Yes/No
  category?: string; // Boolean type thing as well?
  upvotes: number; //There should be an upvote object
  downvotes: number;
  organization_id?: number; // Change type to organization?
}

export interface BackPost {
  id: number | null;
  headline: string;
  synopsis?: string; // Optional
  main_story: string;
  author: number; // Change type to user
  slug: string;
  state: String; // Boolean type thing? Draft, Published.
  image_url?: string;
  publish_date: String;
  mod_date: String;
  announcement: boolean; // Yes/No
  category?: string; // Boolean type thing as well?
  upvotes: number; //There should be an upvote object
  downvotes: number;
  organization_id?: number; // Change type to organization?
}

/*export const posts: Post[] = [
  {
    id: 1,
    headline: 'New Technology Trends',
    synopsis: 'Discover the latest advancements in technology.',
    mainStory: 'This is a post about technology trends.',
    author: 'John Doe',
    organization: 'Tech Company',
    state: 'Draft',
    slug: 'new-technology-trends',
    publishDate: '2023-01-01',
    modificationDate: '2023-01-02',
    announcement: true,
    category: 'Technology',
    upvotes: 10,
    downvotes: 2
  },
  {
    id: 2,
    headline: 'Breaking News: COVID-19 Updates',
    mainStory: 'Stay informed about COVID-19 developments.',
    author: 'Jane Smith',
    state: 'Draft',
    slug: 'covid-19-updates',
    publishDate: '2023-02-01',
    modificationDate: '2023-02-02',
    announcement: false,
    upvotes: 5,
    downvotes: 1
  }
  // Add more sample posts
];
*/
