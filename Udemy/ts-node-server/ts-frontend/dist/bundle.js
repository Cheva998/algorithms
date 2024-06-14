/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./src/Router.ts":
/*!***********************!*\
  !*** ./src/Router.ts ***!
  \***********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Router = void 0;
const Home_1 = __webpack_require__(/*! ./components/Home */ "./src/components/Home.ts");
const Login_1 = __webpack_require__(/*! ./components/Login */ "./src/components/Login.ts");
class Router {
    constructor() {
        this.mainElement = document.getElementById('main-container');
    }
    handleRequest() {
        var _a, _b;
        const location = this.getRoute();
        console.log(`Handling request for ${location}`);
        switch (location) {
            case '/Udemy/ts-node-server/ts-frontend/login':
                (_a = this.mainElement) === null || _a === void 0 ? void 0 : _a.append(new Login_1.Login().render());
                break;
            default:
                (_b = this.mainElement) === null || _b === void 0 ? void 0 : _b.append(new Home_1.Home().render());
                break;
        }
    }
    ;
    getRoute() {
        return window.location.pathname;
    }
    ;
}
exports.Router = Router;
;


/***/ }),

/***/ "./src/components/Home.ts":
/*!********************************!*\
  !*** ./src/components/Home.ts ***!
  \********************************/
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Home = void 0;
class Home {
    constructor() {
        this.container = document.createElement('div');
    }
    render() {
        const pageLabel = document.createElement('label');
        pageLabel.innerText = "Welcome to Home page";
        this.container.append(pageLabel);
        return this.container;
    }
}
exports.Home = Home;


/***/ }),

/***/ "./src/components/Login.ts":
/*!*********************************!*\
  !*** ./src/components/Login.ts ***!
  \*********************************/
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Login = void 0;
class Login {
    constructor() {
        this.container = document.createElement('div');
    }
    render() {
        const pageLabel = document.createElement('label');
        pageLabel.innerText = 'Welcome to the Login';
        this.container.append(pageLabel);
        return this.container;
    }
}
exports.Login = Login;


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it uses a non-standard name for the exports (exports).
(() => {
var exports = __webpack_exports__;
/*!*************************!*\
  !*** ./src/Launcher.ts ***!
  \*************************/

Object.defineProperty(exports, "__esModule", ({ value: true }));
const Router_1 = __webpack_require__(/*! ./Router */ "./src/Router.ts");
class Launcher {
    constructor() {
        this.router = new Router_1.Router();
    }
    launchApp() {
        console.log('App started');
        this.router.handleRequest();
    }
    ;
}
;
new Launcher().launchApp();

})();

/******/ })()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiYnVuZGxlLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7QUFBQSx3RkFBeUM7QUFDekMsMkZBQTJDO0FBSTNDLE1BQWEsTUFBTTtJQUFuQjtRQUVZLGdCQUFXLEdBQUcsUUFBUSxDQUFDLGNBQWMsQ0FBQyxnQkFBZ0IsQ0FBQyxDQUFDO0lBbUJwRSxDQUFDO0lBakJVLGFBQWE7O1FBQ2hCLE1BQU0sUUFBUSxHQUFHLElBQUksQ0FBQyxRQUFRLEVBQUUsQ0FBQztRQUNqQyxPQUFPLENBQUMsR0FBRyxDQUFDLHdCQUF3QixRQUFRLEVBQUUsQ0FBQyxDQUFDO1FBQ2hELFFBQVEsUUFBUSxFQUFFLENBQUM7WUFDZixLQUFLLHlDQUF5QztnQkFDMUMsVUFBSSxDQUFDLFdBQVcsMENBQUUsTUFBTSxDQUFDLElBQUksYUFBSyxFQUFFLENBQUMsTUFBTSxFQUFFLENBQUMsQ0FBQztnQkFDL0MsTUFBTTtZQUVWO2dCQUNJLFVBQUksQ0FBQyxXQUFXLDBDQUFFLE1BQU0sQ0FBQyxJQUFJLFdBQUksRUFBRSxDQUFDLE1BQU0sRUFBRSxDQUFDLENBQUM7Z0JBQzlDLE1BQU07UUFDZCxDQUFDO0lBQ0wsQ0FBQztJQUFBLENBQUM7SUFFTSxRQUFRO1FBQ1osT0FBTyxNQUFNLENBQUMsUUFBUSxDQUFDLFFBQVEsQ0FBQztJQUNwQyxDQUFDO0lBQUEsQ0FBQztDQUNMO0FBckJELHdCQXFCQztBQUFBLENBQUM7Ozs7Ozs7Ozs7Ozs7O0FDdEJGLE1BQWEsSUFBSTtJQUFqQjtRQUNZLGNBQVMsR0FBRyxRQUFRLENBQUMsYUFBYSxDQUFDLEtBQUssQ0FBQyxDQUFDO0lBUXRELENBQUM7SUFORyxNQUFNO1FBQ0YsTUFBTSxTQUFTLEdBQUcsUUFBUSxDQUFDLGFBQWEsQ0FBQyxPQUFPLENBQUMsQ0FBQztRQUNsRCxTQUFTLENBQUMsU0FBUyxHQUFHLHNCQUFzQixDQUFDO1FBQzdDLElBQUksQ0FBQyxTQUFTLENBQUMsTUFBTSxDQUFDLFNBQVMsQ0FBQyxDQUFDO1FBQ2pDLE9BQU8sSUFBSSxDQUFDLFNBQVMsQ0FBQztJQUMxQixDQUFDO0NBQ0o7QUFURCxvQkFTQzs7Ozs7Ozs7Ozs7Ozs7QUNWRCxNQUFhLEtBQUs7SUFBbEI7UUFFWSxjQUFTLEdBQUcsUUFBUSxDQUFDLGFBQWEsQ0FBQyxLQUFLLENBQUMsQ0FBQztJQVF0RCxDQUFDO0lBTkcsTUFBTTtRQUNGLE1BQU0sU0FBUyxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsT0FBTyxDQUFDLENBQUM7UUFDbEQsU0FBUyxDQUFDLFNBQVMsR0FBRyxzQkFBc0IsQ0FBQztRQUM3QyxJQUFJLENBQUMsU0FBUyxDQUFDLE1BQU0sQ0FBQyxTQUFTLENBQUMsQ0FBQztRQUNqQyxPQUFPLElBQUksQ0FBQyxTQUFTLENBQUM7SUFDMUIsQ0FBQztDQUNKO0FBVkQsc0JBVUM7Ozs7Ozs7VUNiRDtVQUNBOztVQUVBO1VBQ0E7VUFDQTtVQUNBO1VBQ0E7VUFDQTtVQUNBO1VBQ0E7VUFDQTtVQUNBO1VBQ0E7VUFDQTtVQUNBOztVQUVBO1VBQ0E7O1VBRUE7VUFDQTtVQUNBOzs7Ozs7Ozs7Ozs7QUN0QkEsd0VBQWtDO0FBS2xDLE1BQU0sUUFBUTtJQUFkO1FBRVksV0FBTSxHQUFXLElBQUksZUFBTSxFQUFFLENBQUM7SUFLMUMsQ0FBQztJQUpVLFNBQVM7UUFDWixPQUFPLENBQUMsR0FBRyxDQUFDLGFBQWEsQ0FBQyxDQUFDO1FBQzNCLElBQUksQ0FBQyxNQUFNLENBQUMsYUFBYSxFQUFFLENBQUM7SUFDaEMsQ0FBQztJQUFBLENBQUM7Q0FDTDtBQUFBLENBQUM7QUFFRixJQUFJLFFBQVEsRUFBRSxDQUFDLFNBQVMsRUFBRSxDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vdHMtZnJvbnRlbmQvLi9zcmMvUm91dGVyLnRzIiwid2VicGFjazovL3RzLWZyb250ZW5kLy4vc3JjL2NvbXBvbmVudHMvSG9tZS50cyIsIndlYnBhY2s6Ly90cy1mcm9udGVuZC8uL3NyYy9jb21wb25lbnRzL0xvZ2luLnRzIiwid2VicGFjazovL3RzLWZyb250ZW5kL3dlYnBhY2svYm9vdHN0cmFwIiwid2VicGFjazovL3RzLWZyb250ZW5kLy4vc3JjL0xhdW5jaGVyLnRzIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7IEhvbWUgfSBmcm9tIFwiLi9jb21wb25lbnRzL0hvbWVcIjtcbmltcG9ydCB7IExvZ2luIH0gZnJvbSBcIi4vY29tcG9uZW50cy9Mb2dpblwiO1xuXG5cblxuZXhwb3J0IGNsYXNzIFJvdXRlciB7XG4gICAgXG4gICAgcHJpdmF0ZSBtYWluRWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdtYWluLWNvbnRhaW5lcicpO1xuXG4gICAgcHVibGljIGhhbmRsZVJlcXVlc3QoKSB7XG4gICAgICAgIGNvbnN0IGxvY2F0aW9uID0gdGhpcy5nZXRSb3V0ZSgpO1xuICAgICAgICBjb25zb2xlLmxvZyhgSGFuZGxpbmcgcmVxdWVzdCBmb3IgJHtsb2NhdGlvbn1gKTtcbiAgICAgICAgc3dpdGNoIChsb2NhdGlvbikge1xuICAgICAgICAgICAgY2FzZSAnL1VkZW15L3RzLW5vZGUtc2VydmVyL3RzLWZyb250ZW5kL2xvZ2luJzogXG4gICAgICAgICAgICAgICAgdGhpcy5tYWluRWxlbWVudD8uYXBwZW5kKG5ldyBMb2dpbigpLnJlbmRlcigpKTtcbiAgICAgICAgICAgICAgICBicmVhaztcbiAgICAgICAgICAgIFxuICAgICAgICAgICAgZGVmYXVsdDpcbiAgICAgICAgICAgICAgICB0aGlzLm1haW5FbGVtZW50Py5hcHBlbmQobmV3IEhvbWUoKS5yZW5kZXIoKSk7XG4gICAgICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgIH1cbiAgICB9O1xuXG4gICAgcHJpdmF0ZSBnZXRSb3V0ZSgpIHtcbiAgICAgICAgcmV0dXJuIHdpbmRvdy5sb2NhdGlvbi5wYXRobmFtZTtcbiAgICB9O1xufTsiLCJcblxuXG5cbmV4cG9ydCBjbGFzcyBIb21lIHtcbiAgICBwcml2YXRlIGNvbnRhaW5lciA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2RpdicpO1xuXG4gICAgcmVuZGVyKCkge1xuICAgICAgICBjb25zdCBwYWdlTGFiZWwgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsYWJlbCcpO1xuICAgICAgICBwYWdlTGFiZWwuaW5uZXJUZXh0ID0gXCJXZWxjb21lIHRvIEhvbWUgcGFnZVwiO1xuICAgICAgICB0aGlzLmNvbnRhaW5lci5hcHBlbmQocGFnZUxhYmVsKTtcbiAgICAgICAgcmV0dXJuIHRoaXMuY29udGFpbmVyO1xuICAgIH1cbn0iLCJcblxuXG5leHBvcnQgY2xhc3MgTG9naW4ge1xuXG4gICAgcHJpdmF0ZSBjb250YWluZXIgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdkaXYnKTtcblxuICAgIHJlbmRlcigpIHtcbiAgICAgICAgY29uc3QgcGFnZUxhYmVsID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnbGFiZWwnKTtcbiAgICAgICAgcGFnZUxhYmVsLmlubmVyVGV4dCA9ICdXZWxjb21lIHRvIHRoZSBMb2dpbic7XG4gICAgICAgIHRoaXMuY29udGFpbmVyLmFwcGVuZChwYWdlTGFiZWwpO1xuICAgICAgICByZXR1cm4gdGhpcy5jb250YWluZXI7XG4gICAgfVxufSIsIi8vIFRoZSBtb2R1bGUgY2FjaGVcbnZhciBfX3dlYnBhY2tfbW9kdWxlX2NhY2hlX18gPSB7fTtcblxuLy8gVGhlIHJlcXVpcmUgZnVuY3Rpb25cbmZ1bmN0aW9uIF9fd2VicGFja19yZXF1aXJlX18obW9kdWxlSWQpIHtcblx0Ly8gQ2hlY2sgaWYgbW9kdWxlIGlzIGluIGNhY2hlXG5cdHZhciBjYWNoZWRNb2R1bGUgPSBfX3dlYnBhY2tfbW9kdWxlX2NhY2hlX19bbW9kdWxlSWRdO1xuXHRpZiAoY2FjaGVkTW9kdWxlICE9PSB1bmRlZmluZWQpIHtcblx0XHRyZXR1cm4gY2FjaGVkTW9kdWxlLmV4cG9ydHM7XG5cdH1cblx0Ly8gQ3JlYXRlIGEgbmV3IG1vZHVsZSAoYW5kIHB1dCBpdCBpbnRvIHRoZSBjYWNoZSlcblx0dmFyIG1vZHVsZSA9IF9fd2VicGFja19tb2R1bGVfY2FjaGVfX1ttb2R1bGVJZF0gPSB7XG5cdFx0Ly8gbm8gbW9kdWxlLmlkIG5lZWRlZFxuXHRcdC8vIG5vIG1vZHVsZS5sb2FkZWQgbmVlZGVkXG5cdFx0ZXhwb3J0czoge31cblx0fTtcblxuXHQvLyBFeGVjdXRlIHRoZSBtb2R1bGUgZnVuY3Rpb25cblx0X193ZWJwYWNrX21vZHVsZXNfX1ttb2R1bGVJZF0obW9kdWxlLCBtb2R1bGUuZXhwb3J0cywgX193ZWJwYWNrX3JlcXVpcmVfXyk7XG5cblx0Ly8gUmV0dXJuIHRoZSBleHBvcnRzIG9mIHRoZSBtb2R1bGVcblx0cmV0dXJuIG1vZHVsZS5leHBvcnRzO1xufVxuXG4iLCJpbXBvcnQgeyBSb3V0ZXIgfSBmcm9tIFwiLi9Sb3V0ZXJcIjtcblxuXG5cblxuY2xhc3MgTGF1bmNoZXIge1xuXG4gICAgcHJpdmF0ZSByb3V0ZXI6IFJvdXRlciA9IG5ldyBSb3V0ZXIoKTtcbiAgICBwdWJsaWMgbGF1bmNoQXBwKCkge1xuICAgICAgICBjb25zb2xlLmxvZygnQXBwIHN0YXJ0ZWQnKTtcbiAgICAgICAgdGhpcy5yb3V0ZXIuaGFuZGxlUmVxdWVzdCgpO1xuICAgIH07XG59O1xuXG5uZXcgTGF1bmNoZXIoKS5sYXVuY2hBcHAoKTsiXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=