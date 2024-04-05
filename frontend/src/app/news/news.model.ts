export interface Post {
  id: number;
  headline: string;
  synopsis?: string; // Optional
  mainStory: string;
  author: String; // Change type to user
  organization?: String; // Change type to organization?
  state: String; // Boolean type thing? Draft, Published.
  slug: string;
  publishDate: Date;
  modificationDate: Date;
  announcement: boolean; // Yes/No
  category?: string; // Boolean type thing as well?
  upvoteObject: String; //There should be an upvote object
}

export const posts: Post[] = [
  {
    id: 1,
    headline: 'New Technology Trends',
    synopsis: 'Discover the latest advancements in technology.',
    mainStory: '# Introduction\n\nThis is a post about technology trends.',
    author: 'John Doe',
    organization: 'Tech Company',
    state: 'Published',
    slug: 'new-technology-trends',
    publishDate: new Date('2023-01-01'),
    modificationDate: new Date('2023-01-02'),
    announcement: true,
    category: 'Technology',
    upvoteObject: 'Upvote Object 1'
  },
  {
    id: 2,
    headline: 'Breaking News: COVID-19 Updates',
    mainStory: '# Latest Updates\n\nStay informed about COVID-19 developments.',
    author: 'Jane Smith',
    state: 'Draft',
    slug: 'covid-19-updates',
    publishDate: new Date('2023-02-01'),
    modificationDate: new Date('2023-02-02'),
    announcement: false,
    upvoteObject: 'Upvote Object 2'
  }
  // Add more sample posts
];
