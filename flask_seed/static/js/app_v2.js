(function() {
  var seedApp;

  seedApp = angular.module('seedApp', []);

  seedApp.controller('seedCtrl', [
    '$scope', '$http', function($scope, $http) {
      return $http.get('/questions').success(function(r) {
        return $scope.questions = r.question_files;
      });
    }
  ]);

}).call(this);

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImluZGV4LmNvZmZlZSJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtBQUFBLE1BQUEsT0FBQTs7QUFBQSxFQUFBLE9BQUEsR0FBVSxPQUFPLENBQUMsTUFBUixDQUFlLFNBQWYsRUFBeUIsRUFBekIsQ0FBVixDQUFBOztBQUFBLEVBQ0EsT0FBTyxDQUFDLFVBQVIsQ0FBbUIsVUFBbkIsRUFBOEI7SUFBQyxRQUFELEVBQVUsT0FBVixFQUMxQixTQUFDLE1BQUQsRUFBUSxLQUFSLEdBQUE7YUFDSSxLQUFLLENBQUMsR0FBTixDQUFVLFlBQVYsQ0FDSyxDQUFDLE9BRE4sQ0FFSSxTQUFDLENBQUQsR0FBQTtlQUNJLE1BQU0sQ0FBQyxTQUFQLEdBQWtCLENBQUMsQ0FBQyxlQUR4QjtNQUFBLENBRkosRUFESjtJQUFBLENBRDBCO0dBQTlCLENBREEsQ0FBQTtBQUFBIiwiZmlsZSI6ImFwcF92Mi5qcyIsInNvdXJjZXNDb250ZW50IjpbInNlZWRBcHAgPSBhbmd1bGFyLm1vZHVsZSAnc2VlZEFwcCcsW11cbnNlZWRBcHAuY29udHJvbGxlciAnc2VlZEN0cmwnLFsnJHNjb3BlJywnJGh0dHAnLFxuICAgICgkc2NvcGUsJGh0dHApIC0+XG4gICAgICAgICRodHRwLmdldCgnL3F1ZXN0aW9ucycpXG4gICAgICAgICAgICAgLnN1Y2Nlc3MoIFxuICAgICAgICAgICAgKHIpIC0+XG4gICAgICAgICAgICAgICAgJHNjb3BlLnF1ZXN0aW9ucz0gci5xdWVzdGlvbl9maWxlc1xuICAgICAgICAgICAgKVxuXG5dXG4iXSwic291cmNlUm9vdCI6Ii9zb3VyY2UvIn0=