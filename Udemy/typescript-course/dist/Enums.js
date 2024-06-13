"use strict";
var AuthError;
(function (AuthError) {
    AuthError[AuthError["WRONG_CREDENTIALS"] = 0] = "WRONG_CREDENTIALS";
    AuthError[AuthError["SERVER_FAIL"] = 1] = "SERVER_FAIL";
    AuthError[AuthError["EXPIRED_SESSION"] = 2] = "EXPIRED_SESSION";
})(AuthError || (AuthError = {}));
