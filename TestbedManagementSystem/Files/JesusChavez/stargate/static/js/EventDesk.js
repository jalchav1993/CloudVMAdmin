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
 * Polymorphism rocks all the way
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
	var WorkshopGroup = function(){
		this.worgkshop_group_name = ''
	  this.numbreps_workshop = ''
	  this.host_ip = ''
	  this.status_s = ''
	  this.workshop_description = ''
	  this.workshop_unit_list = []
	}
	/* Author: Jesus Chavez
	 * Global factory, handles http requests to rest
	 */
	function global($rootScope, $http) {
		var obj = {};
		obj.busy = "";
		obj.menuItemList = [];
		obj.userItemList = [];
		obj.eventItemList = [];
		obj.requestItemList = [];
		obj.state = [];
		obj.header = [];
		obj.report = [];
		obj.workshopGroupList = [];
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
			$rootScope.$broadcast("isbusy");
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
		obj.getAllWorkshopGroups =function (){
			obj.workshopGroupList = [];
			$http({
				url: "http://" + location.host + "/workshop/getAll/",
				method: "GET"
			}).success(function(data, status, headers, config) {
				for (i = 0; i < data.length; i++) {
					tmp = new WorkshopGroup();
					angular.copy(data[i], tmp);
					obj.workshopGroupList.push(tmp);
					$rootScope.$broadcast("populate-wg");
				};
			}).error(function(data, status, headers, config) {
				console.log('Error');
				console.log(response);
			});
		}
		obj.showAddVmModal = function(){
			console.log("calling the modal")
			$rootScope.$broadcast("isbusy");
			$rootScope.$broadcast('showAddVmModal');
		};
		obj.showAddServerModal = function(){
			console.log("calling the modal")
			$rootScope.$broadcast("isbusy");
			$rootScope.$broadcast('showAddServerModal');
		};
		obj.showLoginModal = function(){
			console.log("calling the modal")
			$rootScope.$broadcast("isbusy");
			$rootScope.$broadcast('showLoginModal');
		};
		obj.showAddWgModal = function(){
			console.log("calling the modal")
			$rootScope.$broadcast("isbusy");
			$rootScope.$broadcast('showAddWgModal');
		};
		obj.showToggleCloneVmModal = function(){
			console.log("calling the modal")
			$rootScope.$broadcast("isbusy");
			$rootScope.$broadcast('showCloneModal');
		}
		obj.busyOff = function(){
			$rootScope.$broadcast('notbusy');
		}
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
			templateUrl: './templates/workshop_groups/',
			controller: 'wsgController'
		}).when('/wsuRt', {
			templateUrl: './templates/workshop_units/',
			controller: 'wsuController'
		});
		// configure html5 to get links working on jsfiddle
		$locationProvider.html5Mode(true);
	};
	/* Author: Jesus Chavez
	 * Controller for side nav
	 */
	function navCtrl($scope, $mdSidenav, $timeout, global, $route) {
		var originatorEv, mdOpenThis;
		busy = true;
		global.initRequest();
		$scope.isloading = function (){
			return busy;
		}
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
		$scope.$on("isbusy", function(){
			busy = true;
		});
		$scope.$on("notbusy", function(){
			console.log(busy);
			busy = false;
		});
		$scope.$on("populate-init", function(){
			populate_right();
			global.busyOff();
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
				
				global.showLoginModal();
			} else if (a == 'signout') {
				global.signOut();
			}else if (a == 'server'){
				//global.getUsers();
			} else if (a === 'vm'){
				//global.addEvent();
			} else if (a === 'wg'){
				//global.addUser();
			} else if (a === 'wu'){
				//global.addUser();
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
		
		$scope.$on('showLoginModal', function() {
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
				global.busyOff();
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
	function AddServerModalCtrl($uibModal, $scope, $log, $document, global){
		var $ctrl = this;
		$ctrl.animationsEnabled = true;
		$ctrl.selectedItem;
		$scope.$on('showAddServerModal', function(){
			console.log('what');
			var parentElem = angular.element($document[0].querySelector('.modal-server'));
			var modalInstance = $uibModal.open({
					animation: $ctrl.animationsEnabled,
					ariaLabelledBy: 'modal-title',
					ariaDescribedBy: 'modal-event',
					templateUrl: 'templates/panel/AddServerPanel.html',
					controller: 'AddServerModalInstanceCtrl',
					controllerAs: '$ctrl',
					size: 'sm',
					appendTo: parentElem
			});
			modalInstance.result.then(function(selectedItem) {
				$ctrl.selected = selectedItem;
			}, function() {
				global.busyOff();
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
	function AddVmModalCtrl ($uibModal, $scope, $log, $document, global){
		var $ctrl = this;
		$ctrl.animationsEnabled = true;
		$ctrl.selectedItem;
		$scope.$on('showAddVmModal', function(){
			console.log('what');
			var parentElem = angular.element($document[0].querySelector('.modal-vm'));
			var modalInstance = $uibModal.open({
					animation: $ctrl.animationsEnabled,
					ariaLabelledBy: 'modal-title',
					ariaDescribedBy: 'modal-event',
					templateUrl: 'templates/panel/AddVmPanel.html',
					controller: 'AddVmInstaceModalCtrl',
					controllerAs: '$ctrl',
					size: 'lg',
					appendTo: parentElem
			});
			modalInstance.result.then(function(selectedItem) {
				$ctrl.selected = selectedItem;
			}, function() {
				global.busyOff();
				$log.info('Modal was dismissed at: ' + new Date());
			});
		});
	}
	function AddVmInstaceModalCtrl ($uibModalInstance, $scope, $timeout, global){
		var $ctrl = this;
		$ctrl.is = "it";
		/*This will be loaded dinamically using global functions, will be using placeholder values rn*/
		$ctrl.vm = ['Virtual Machine 1',
						'Virtual Machine 2',
						'Virtual Machine 3',
						'Virtual Machine 4' ];
		/* This will be used to store the virtual machines selected*/
		$ctrl.slected_vm = [];
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
	}
	function CloneVmModalCtrl($uibModal, $scope, $log, $document, global){
		var $ctrl = this;
		$ctrl.animationsEnabled = true;
		$ctrl.selectedItem;
		$scope.$on('showCloneModal', function(){
			var parentElem = angular.element($document[0].querySelector('.modal-clonevm'));
			var modalInstance = $uibModal.open({
					animation: $ctrl.animationsEnabled,
					ariaLabelledBy: 'modal-title',
					ariaDescribedBy: 'modal-event',
					templateUrl: 'templates/panel/CloneVmPanel.html',
					controller: 'CloneVmInstanceModalCtrl',
					controllerAs: '$ctrl',
					size: 'lg',
					appendTo: parentElem
			});
			modalInstance.result.then(function(selectedItem) {
				$ctrl.selected = selectedItem;
			}, function() {
				global.busyOff();
				$log.info('Modal was dismissed at: ' + new Date());
			});
		});
	}
	function CloneVmInstanceModalCtrl($uibModalInstance, $scope, $timeout, global){
		var $ctrl = this;
	}
	function AddWgModalCtrl ($uibModal, $scope, $log, $document, global){
		var $ctrl = this;
		$ctrl.animationsEnabled = true;
		$ctrl.selectedItem;
		$scope.$on('showAddWgModal', function(){
			console.log('what');
			var parentElem = angular.element($document[0].querySelector('.modal-wg'));
			var modalInstance = $uibModal.open({
					animation: $ctrl.animationsEnabled,
					ariaLabelledBy: 'modal-title',
					ariaDescribedBy: 'modal-event',
					templateUrl: 'templates/panel/AddWgPanel.html',
					controller: 'AddWgInstanceModalCtrl',
					controllerAs: '$ctrl',
					size: 'lg',
					appendTo: parentElem
			});
			modalInstance.result.then(function(selectedItem) {
				$ctrl.selected = selectedItem;
			}, function() {
				global.busyOff();
				$log.info('Modal was dismissed at: ' + new Date());
			});
		});
	}
	function AddWgInstanceModalCtrl($uibModalInstance, $scope, $timeout, global){
		var $ctrl = this;
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
		
	}
	function blackModalInstanceConfig($mdThemingProvider){
		$mdThemingProvider.theme('docs-dark', 'default')
      .primaryPalette('yellow')
      .dark();
		
	}
	function serversController($route, $routeParams, $location, $scope, global) {
		$scope.toggleAddServerModal=function(){
			global.showAddServerModal();
		};
	};
	function vmController($route, $routeParams, $location, $scope, global) {
		$scope.toggleAddVmModal = function(){
			global.showAddVmModal();
		};
		$scope.toggleCloneVmModal = function () {
			global.showToggleCloneVmModal();
		};
	};
	function wsgController($route, $routeParams, $location, $scope, global) {
		global.getAllWorkshopGroups();
		$scope.toggleAddWgModal = function(){
			global.showAddWgModal();
		};
		$scope.$on('populate-wg', function(){
			$scope.workshop_gp = [];
			$scope.workshop_gp = global.workshopGroupList;
		});
	};
	function wsuController($route, $routeParams, $location, $scope, global) {
		
	};
	function profilesController($route, $routeParams, $location, $scope, global) {

	};

	app.controller('navCtrl', navCtrl);
	app.controller('AddVmModalCtrl', AddVmModalCtrl);
	app.controller('AddVmInstaceModalCtrl', AddVmInstaceModalCtrl);
	app.controller('CloneVmModalCtrl', CloneVmModalCtrl);
	app.controller('CloneVmInstanceModalCtrl', CloneVmModalCtrl);
	app.controller('AddWgModalCtrl', AddWgModalCtrl);
	app.controller('AddWgInstanceModalCtrl', AddWgInstanceModalCtrl);
	app.controller('loginModalCtrl', loginModalCtrl);
	app.controller('loginModalInstanceCtrl', loginModalInstanceCtrl);
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
