

class BlogPost {
    // title: string;
    // content: string;
  
    constructor(public title: string, public content: string) {
      this.title = title;
      this.content = content;
    }
  
    // Methods related to content management
    createPost() {
      // Implementation here
    }
  
    updatePost() {
      // Implementation here
    }
  
    deletePost() {
      // Implementation here
    }
}

class RenderPost {
    constructor(private blogPost: BlogPost) {}
    // Method related to post display
    displayHTML() {
      return `<h1>${this.blogPost.title}</h1><p>${this.blogPost.content}</p>`;
    }
  }

  const blog = new BlogPost('title', 'some content')
  const renderBlog = new RenderPost(blog)
  console.log(renderBlog.displayHTML())