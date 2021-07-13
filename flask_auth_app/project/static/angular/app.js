(function () {
  'use strict';


  angular.module('Searchapp', [])
  .controller('SearchappController', SearchappController);

SearchappController.$inject = ['$scope'];
function SearchappController($scope) {
  $scope.search = "";
  $scope.search2 = "";
  $scope.h1color = "";
  $scope.Loginstatus = "";
  $scope.searchingfunction = function () {
    if ($scope.search < 1) {
    $scope.display = "none";
    $scope.search2 = "Please Enter Data First";
    $scope.h1color = "red";
  }
  else {
    $scope.display = "block";
    $scope.search2 = "Showing Results For ";
    $scope.search2 += $scope.search;
    $scope.h1color = "whitesmoke";
  };

  if (document.getElementsByClassName('login').innerHTML = "Login") {
    $scope.Loginstatus = "Please Log In First!";
  }
  else {
    $scope.Loginstatus = "On Maintainance";
  };
  };
};


})();
