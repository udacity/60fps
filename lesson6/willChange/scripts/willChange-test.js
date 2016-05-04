(function() {
  UdacityFEGradingEngine.turnOn();
  UdacityFEGradingEngine.registerSuites(`[
    {
      "name": "will-change",
      "code": "willwhatchange?",
      "tests": [
        {
          "description": "All the boxes are on the page.",
          "definition": {
            "nodes": ".box",
            "get": "count",
            "equals": 120
          }
        },
        {
          "description": "Elements of class 'box' are will-changed.",
          "definition": {
            "nodes": ".box",
            "cssProperty": "will-change",
            "equals": "transform"
          }
        }
      ]
    }
  ]`);
})();