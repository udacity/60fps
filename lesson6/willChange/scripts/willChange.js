var suites = [
  {
    name: "will-change",
    code: "willwhatchange?",
    tests: [
      {
        func: "testDOMelemCount",
        params: [
          {
            selector: ".box",
            count: 120
          }
        ],
        desc: "All the boxes are on the page."
      },
      {
        func: "testDOMelemCSS",
        params: [
          {
            selector: ".box",
            property: "will-change",
            value: "transform"
          }
        ],
        desc: "Elements of class 'box' are will-changed."
      }
    ]
  }
]

var graderProperties = {
  suites: suites
}