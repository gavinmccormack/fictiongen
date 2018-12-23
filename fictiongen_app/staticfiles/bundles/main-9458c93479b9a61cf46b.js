/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./fictiongen_app/staticfiles/js/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./fictiongen_app/staticfiles/js/index.js":
/*!************************************************!*\
  !*** ./fictiongen_app/staticfiles/js/index.js ***!
  \************************************************/
/*! no exports provided */
/***/ (function(module, exports) {

eval("throw new Error(\"Module build failed (from ./node_modules/babel-loader/lib/index.js):\\nSyntaxError: /mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/fictiongen_app/staticfiles/js/index.js: Unexpected token, expected \\\";\\\" (3:35)\\n\\n\\u001b[0m \\u001b[90m 1 | \\u001b[39m\\u001b[36mimport\\u001b[39m \\u001b[33mReact\\u001b[39m from \\u001b[32m'react'\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 2 | \\u001b[39m\\u001b[36mimport\\u001b[39m \\u001b[33mReactDOM\\u001b[39m from \\u001b[32m'react-dom'\\u001b[39m\\u001b[0m\\n\\u001b[0m\\u001b[31m\\u001b[1m>\\u001b[22m\\u001b[39m\\u001b[90m 3 | \\u001b[39m\\u001b[36mimport\\u001b[39m \\u001b[33mDataInterface\\u001b[39m from \\u001b[32m'./data'\\u001b[39m as data\\u001b[0m\\n\\u001b[0m \\u001b[90m   | \\u001b[39m                                   \\u001b[31m\\u001b[1m^\\u001b[22m\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 4 | \\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 5 | \\u001b[39m\\u001b[90m// Settings; to be hooked into room settings / etc but for now can be per session \\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 6 | \\u001b[39m\\u001b[36mconst\\u001b[39m settingsArea \\u001b[33m=\\u001b[39m \\u001b[33m<\\u001b[39m\\u001b[33minputArea\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[33m<\\u001b[39m\\u001b[33minput\\u001b[39m \\u001b[36mclass\\u001b[39m\\u001b[33m=\\u001b[39m\\u001b[32m'checkbox'\\u001b[39m id\\u001b[33m=\\u001b[39m\\u001b[32m'grammar-entry'\\u001b[39m type\\u001b[33m=\\u001b[39m\\u001b[32m'checkbox'\\u001b[39m \\u001b[33m/\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[33m<\\u001b[39m\\u001b[33mspan\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[33m<\\u001b[39m\\u001b[33m/\\u001b[39m\\u001b[33mspan\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[33m<\\u001b[39m\\u001b[33mlabel\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[33mLabel\\u001b[39m \\u001b[33mOf\\u001b[39m \\u001b[33mThing\\u001b[39m\\u001b[33m<\\u001b[39m\\u001b[33m/\\u001b[39m\\u001b[33mlabel\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[33m<\\u001b[39m\\u001b[33m/\\u001b[39m\\u001b[33minputArea\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[33m;\\u001b[39m\\u001b[0m\\n    at _class.raise (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:4051:15)\\n    at _class.unexpected (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:5382:16)\\n    at _class.semicolon (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:5366:40)\\n    at _class.parseImport (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:8827:10)\\n    at _class.parseStatementContent (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:7586:27)\\n    at _class.parseStatement (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:7505:17)\\n    at _class.parseBlockOrModuleBlockBody (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:8073:23)\\n    at _class.parseBlockBody (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:8060:10)\\n    at _class.parseTopLevel (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:7470:10)\\n    at _class.parse (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:8915:17)\\n    at parse (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/parser/lib/index.js:10946:38)\\n    at parser (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/core/lib/transformation/normalize-file.js:170:34)\\n    at normalizeFile (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/core/lib/transformation/normalize-file.js:138:11)\\n    at runSync (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/core/lib/transformation/index.js:44:43)\\n    at runAsync (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/core/lib/transformation/index.js:35:14)\\n    at process.nextTick (/mnt/c/Users/gavin/Desktop/fictiongen/fictiongen/node_modules/@babel/core/lib/transform.js:34:34)\\n    at _combinedTickCallback (internal/process/next_tick.js:132:7)\\n    at process._tickCallback (internal/process/next_tick.js:181:9)\");\n\n//# sourceURL=webpack:///./fictiongen_app/staticfiles/js/index.js?");

/***/ })

/******/ });