

enum AuthError {
    WRONG_CREDENTIALS,
    SERVER_FAIL,
    EXPIRED_SESSION,
    UNEXPECTED_ERROR
}

console.log(AuthError[AuthError.WRONG_CREDENTIALS]);


enum AuthError2 {
    WRONG_CREDENTIALS = 'wrong credentials',
    SERVER_FAIL = 'server fail',
    EXPIRED_SESSION = 'expired session'
}

console.log(AuthError2.WRONG_CREDENTIALS);

function handleError(error: AuthError){
    switch (error) {
        case AuthError.EXPIRED_SESSION:
            console.log('get new session');
            break;
        case AuthError.SERVER_FAIL:
            console.log('restart server');
            break;
        case AuthError.WRONG_CREDENTIALS:
        case AuthError.UNEXPECTED_ERROR:
            console.log('check input');
            break;
        default:
            break;
    }
}


handleError(AuthError.SERVER_FAIL)
