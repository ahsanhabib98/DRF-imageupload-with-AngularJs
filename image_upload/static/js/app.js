// var myApp = angular.module('imageuploadApp', ['ngResource']);

// myApp.config(function($resourceProvider) {
// 	$resourceProvider.defaults.stripTrailingSlashes = false;
// });

// myApp.controller('MainCtrl', function($scope, $http)
// {
// 	$http.get('/api/images/').then(function(response) {
// 		$scope.images = [];
// 		for (var i = 0; i < response.data.length; i++) {

// 			var image = {};
// 			image.image = response.data[i].image
// 			image.pk = response.data[i].pk
// 			$scope.images.push(image);
// 			console.log(response)
// 		}
// 	});
// });


var myApp = angular.module('imageuploadApp', ['ngResource', 'ngFileUpload']);

myApp.config(function($resourceProvider) {
	$resourceProvider.defaults.stripTrailingSlashes = false;
});

myApp.controller('MainCtrl', function($scope, Images)
{
	console.log('In main control')
	$scope.images = Images.query();

	$scope.newImage = {};

	$scope.deleteImage = function(image)
	{
		image.$delete(
			function(response) {
				$scope.images = Images.query();
			}
		);
	};

	$scope.uploadImage = function()
	{
		console.log('Upload Image called.')
		Images.save($scope.newImage).$promise.then(
			function(response) {

				$scope.newImage = {};

				$scope.images.unshift(response);
			}
		);
	};
});





