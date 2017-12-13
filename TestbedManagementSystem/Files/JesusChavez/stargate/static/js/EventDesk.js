/*
/* Author: Jesus Chavez
 * POST/GET do not actually reload page, angularjs by google(c) 
 * From mean Plataform, Angular Javascript framework delivers them!!!important!!!
 * POST/GET uses AJAX
 * POST/GET Requests in funtion global(..){..}
 * global handles api requests to api
 * the aplication programing interface was written in PHP, 
 * reference api for any POST/GET Request information,
 * and data base manipulation
 */
(function() {
	//hoisted
	var app = angular.module('EventDesk', ['ngMaterial', 'ngRoute', 'ui.bootstrap','ngMessages']);
	'use strict';
	/*
	/* Author: Jesus Chavez
	 * Menu item object node
	 */
	var MenuItem = function() {
		this.template = '';
		this.action = '';
		this.route = '';
	};
	var HeaderItem = function() {
		this.msg = '';
		this.accordionItems = [];
	};
	var Resonse = function() {
		this.response = '';
	};
	var UserItem = function(){
	 	this.userType= '';
	 	this.userName='';
	 	this.firstName='';
		this.middleInit='';
	  this.lastName='';
		this.userPass='';
		this.telephone='';
		this.eventPreference='';
		this.userClass='';
	}
	var EventItem = function(){
	 	this.eventId= '';
	 	this.eventName='';
	 	this.eventDescription='';
		this.eventLocation='';
	  this.eventVolunteers='';
	  this.approved_by='';
		this.created_by='';
		this.updated_by='';
	}
	var Report= function(){
		this.Eid = '';
		this.Hours = '';
	}
	/* Author: Jesus Chavez
	 * Global factory, handles http requests to rest
	 */
	function global($rootScope, $http) {
		var obj = {};
		obj.menuItemList = [];
		obj.userItemList = [];
		obj.eventItemList = [];
		obj.requestItemList = [];
		obj.state = [];
		obj.header = [];
		obj.report = [];
		obj.loginResponse = "";
		obj.panelRef = "";
		obj.signUp = function(eventId){
			$http({
				url: "http://" + location.host + "/api/sql/insert/volunteer/",
				method: "POST",
				data: {
					request:'insertVolunteerById',
					Eid:eventId
				}
			}).success(function(data, status, headers, config) {
				console.log('got populate response '+data)
				if(data === ' delete-user-success '){
					$rootScope.$broadcast('delete-user-request-accepted');
				}else if(data === 'insert-server-error'){
					$rootScope.$broadcast('delete-user-request-denied');
				}
			}).error(function(data, status, headers, config) {
				console.log('Error this');
				console.log(response);
			});
		}
		obj.initRequest = function(){
			obj.header = [];
			$http({
				url: "http://" + location.host + "/api/init",
				method: "GET"
			}).success(function(data, status, headers, config) {
				tmp = new HeaderItem();
				angular.copy(data[0], tmp);
				obj.header = tmp;
				$rootScope.$broadcast("populate-init");
				console.log("init")
			}).error(function(data, status, headers, config) {
				console.log('Error');
				console.log(response);
			});
		}
		obj.getAndToggleMenu = function() {
			obj.menuItemList = [];
			//obj.header = [];
			$http({
				url: "http://" + location.host + "/api/menu/sidenav",
				method: "GET"
			}).success(function(data, status, headers, config) {
				//tmp = new HeaderItem();
				//angular.copy(data[0], tmp);
				//obj.header = tmp;
				for (i = 0; i < data.length; i++) {
					tmp = new MenuItem();
					angular.copy(data[i], tmp);
					obj.menuItemList.push(tmp);
				}
				$rootScope.$broadcast("populate");
			}).error(function(data, status, headers, config) {
				console.log('Error');
				console.log(response);
			});
		};
		obj.getAndToggleRightMenu =function (){
			obj.header = [];
			$http({
				url: "http://" + location.host + "/api/menu/header",
				method: "GET"
			}).success(function(data, status, headers, config) {
				tmp = new HeaderItem();
				angular.copy(data[0], tmp);
				obj.header = tmp;
				$rootScope.$broadcast("populate-right");
			}).error(function(data, status, headers, config) {
				console.log('Error');
				console.log(response);
			});
		}
		obj.submitSignInRequest = function(formUser, formPwd) {
			$http({
				url: "http://" + location.host + "/api/session/login/",
				method: "POST",
				data: {
					id: formUser,
					pwd: formPwd
				}
			}).success(function(data, status, headers, config) {
				console.log('got populate response '+data)
				if(data ==='login-success'){
					$rootScope.$broadcast("loginSuccess");
				}else if(data ==='login-denied'){
					$rootScope.$broadcast("loginDenied");
				}else{
					$rootScope.$broadcast("loginUnkown");
				}
					
			}).error(function(data, status, headers, config) {
				console.log('Error');
				console.log(response);
			});
		};
		obj.signOut = function() {
			$http({
				url: "http://" + location.host + "/api/session/logout/",
				method: "GET",
			}).success(function(data, status, headers, config) {
				$rootScope.$broadcast("logoutResponse");
			}).error(function(data, status, headers, config) {
				console.log('Error');
				console.log(response);
			});
		}
		obj.showSignInModal = function(){
			console.log("calling the modal")
			$rootScope.$broadcast('showSignInModal');
		};
		return obj;
	};
	function Routes ($routeProvider, $locationProvider) {
		$routeProvider.when('/', {
			templateUrl: './templates/servers/',
		}).when('/serversRt', {
			templateUrl: './templates/servers/',
			controller: 'serversController',
		}).when('/vmRt', {
			templateUrl: './templates/vm/',
			controller: 'vmController'
		}).when('/wsgRt', {
			templateUrl: './templates/wsg/',
			controller: 'wsgController'
		}).when('/wsuRt', {
			templateUrl: './templates/wsu/',
			controller: 'wsuController'
		}).when('/usprRt', {
			templateUrl: './templates/profile/',
			controller: 'profilesController'
		});
		// configure html5 to get links working on jsfiddle
		$locationProvider.html5Mode(true);
	};
	/* Author: Jesus Chavez
	 * Controller for side nav
	 */
	function navCtrl($scope, $mdSidenav, $timeout, global, $route) {
		var originatorEv, mdOpenThis;
		global.initRequest();
		$scope.msg = {
			"msg": "welcome, please sign in"
		};
		$scope.getAndToggleMenu = function() {
			global.getAndToggleMenu();

		};
		$scope.openMenu = function($mdOpenMenu, ev) {
      originatorEv = ev;
			mdOpenThis = $mdOpenMenu;
			global.getAndToggleRightMenu();
    };
		$scope.$on("populate-init", function(){
			populate_right();
		});
		$scope.$on("populate-right", function(){
			populate_right();
			toggle_right();
		});
		$scope.$on("populate", function($mdOpenMenu) {
			populate();
			toggle('left');
		});
		$scope.getAction = function(a) {
			console.log(a);
			if (a == 'signin') {
				global.showSignInModal();
			} else if (a == 'signout') {
				global.signOut();
			}else if (a === 'server'){
				//global.getUsers();
			} else if (a === 'vm'){
				global.addEvent();
			} else if (a === 'wg'){
				global.addUser();
			} else if (a === 'wu'){
				global.addUser();
			}  else if( a === 'stat'){
				$route.reload();
			} else if( a === 'profile'){
				$route.reload();
			} else if( a === 'signout'){
				$route.reload();
			}
		};
		$scope.$on('logoutResponse', function(){
			global.getState();
		});
		function populate() {
			$scope.menuItems = [];
			$scope.menuItems = global.menuItemList;
			//$scope.header = global.header;
			console.log(global.menuItemList);
			//console.log(global.header);
		};

		function toggle(side) {
			$mdSidenav(side).toggle();
		}
		function populate_right() {
			$scope.header = global.header;
			console.log(global.header);
		}
		function toggle_right(){
			mdOpenThis(originatorEv);
		}

	};
	function loginModalCtrl ($uibModal, $scope, $log, $document,global) {
		var $ctrl = this;
		$ctrl.animationsEnabled = true;
		$ctrl.selectedItem;
		
		$scope.$on('showSignInModal', function() {
			console.log("showing modal");
			var parentElem = angular.element($document[0].querySelector('.modal-demo'));
			var modalInstance = $uibModal.open({
					animation: $ctrl.animationsEnabled,
					ariaLabelledBy: 'modal-title',
					ariaDescribedBy: 'modal-body',
					templateUrl: '/templates/panel/panel.tmpl.1.03.html',
					controller: 'loginModalInstanceCtrl',
					controllerAs: '$ctrl',
					size: 'sm',
					appendTo: parentElem
			});
			modalInstance.result.then(function(selectedItem) {
				$ctrl.selected = selectedItem;
				global.getAndToggleMenu();
			}, function() {
				$log.info('Modal was dismissed at: ' + new Date());
			});
		});
	};
	function loginModalInstanceCtrl ($uibModalInstance, $scope, $timeout, $window, global) {
		var $ctrl = this;
		$ctrl.emitItem = '';
		$ctrl.emitItemBk = '';
		$ctrl.state={
			'cssClass':'',
			'msgText':''
		};
		$ctrl.input = {
			'user': '',
			'pass': ''
		};
		$scope.$on('loginSuccess', function() {
			$ctrl.state.msgText = 'login success';
			$ctrl.state.cssClass = '#90EE90';
			$timeout(function() {
				$uibModalInstance.close('loginSuccess');
			}, 500);
		});
		$scope.$on('loginDenied', function() {
			$ctrl.state.msgText = 'login failed, incorrect username/password combination';
			$ctrl.state.cssClass = 'red';
		});
		$ctrl.submitSignInRequest = function() {
			global.submitSignInRequest($ctrl.input.user,$ctrl.input.pass);
			console.log('populating ');
		};
		$ctrl.closeLogInDialog = function() {
			$uibModalInstance.dismiss('close');
		};
	};
	function AddServerModalCtrl($uibModal, $scope, $log, $document){
		var $ctrl = this;
		$ctrl.animationsEnabled = true;
		$ctrl.selectedItem;
		$scope.$on('showAddEventModal', function(){
			console.log('what');
			var parentElem = angular.element($document[0].querySelector('.modal-event'));
			var modalInstance = $uibModal.open({
					animation: $ctrl.animationsEnabled,
					ariaLabelledBy: 'modal-title',
					ariaDescribedBy: 'modal-event',
					templateUrl: 'templates/panel/add/serverPanel.html',
					controller: 'AddServerModalInstanceCtrl',
					controllerAs: '$ctrl',
					size: 'lg',
					appendTo: parentElem
			});
			modalInstance.result.then(function(selectedItem) {
				$ctrl.selected = selectedItem;
			}, function() {
				$log.info('Modal was dismissed at: ' + new Date());
			});
		});
	}
	function AddServerModalInstanceCtrl ($uibModalInstance, $scope, $timeout, global) {
		var $ctrl = this;
    $ctrl.server = {
			'ip': '',
			'wsgroups':'',
			'wsunits':''
		}
		$ctrl.n = 1;
		$ctrl.checkBoxSelected = false;
		$ctrl.isDisabled = false;
		$ctrl.selectTimeSlots = 0;
		$ctrl.submitAddServerRequest = function() {
			global.submitAddServerRequest($ctrl.event);
			console.log($ctrl.event);
		};
		$ctrl.closeLogInDialog = function() {
			console.log($ctrl.event);
			$uibModalInstance.dismiss('close');
		};
		$scope.$on('add-event-request-success', function(){
			$ctrl.state.msgText = 'add-user-request-success';
			$ctrl.state.cssClass = '#90EE90';
			console.log('this should close');
			$timeout(function() {
				global.getEvents('myevents');
				$uibModalInstance.close('closed');
			}, 500);
		});
		$scope.$on('add-event-request-denied', function(){
			$ctrl.state.msgText = 'login failed, incorrect username/password combination';
			$ctrl.state.cssClass = 'red';
		});
	};
	function blackModalInstanceConfig($mdThemingProvider){
		$mdThemingProvider.theme('docs-dark', 'default')
      .primaryPalette('yellow')
      .dark();
		
	}
	function serversController($route, $routeParams, $location, $scope, global) {
		
	};
	function vmController($route, $routeParams, $location, $scope, global) {
		
	};
	function wsgController($route, $routeParams, $location, $scope, global) {
		
	};
	function wsuController($route, $routeParams, $location, $scope, global) {
		
	};
	function profilesController($route, $routeParams, $location) {

	};

	app.controller('navCtrl', navCtrl);
	app.controller('loginModalCtrl', loginModalCtrl);
	app.controller('AddServerModalCtrl', AddServerModalCtrl);
	app.controller('AddServerModalInstanceCtrl', AddServerModalInstanceCtrl);
	app.controller('serversController', serversController);
	app.controller('vmController', vmController);
	app.controller('wsgController', wsgController);
	app.controller('wsuController', wsuController);
	app.controller('profilesController', profilesController);
	app.factory('global', global);
	app.config(Routes);
	app.config(blackModalInstanceConfig);
})(angular);
