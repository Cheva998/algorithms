

interface CreatePost {
    post(text: string): void
}

interface CommentPost {
    comment(text: string): void
}

interface SharePost {
    share(): void
}



class Admin implements CreatePost, CommentPost, SharePost {
    post(text: string): void {
        console.log('post created')
    }

    comment(text: string): void {
        console.log('post commented')
    }

    share(): void {
        console.log('post shared')
    }
}

class RegularUser implements CreatePost, SharePost {
    post(text: string): void {
        console.log('user created post')
    }

    share(): void {
        console.log('user shared post')
    }
}