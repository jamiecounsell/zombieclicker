function APIService($http) {
	this.http = $http

	this.PREFIX = "/api/"
	this.getUnlockURL = function(unlock) {
		return this.PREFIX + unlock + "/"
	}
}

angular.module('zombie').service('api', APIService)

APIService.prototype.getUserData = function(first_argument) {
	// body...
};

APIService.prototype.getUnlockables = function() {
	this.http.get(this.getUnlockURL('weapons'))
	.success(function(res) {
		console.log(res)
	})
}