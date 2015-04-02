/*

Page loads
Grader loads
Throw up a "Please Wait" div
Run function (twice)
Measure both runs. Take average if close, take lower if off by more than 2x.
Use a promise to save the time?
When it runs again, compare the new time. If it meets a criteria, it passes, otherwise, kep waiting.
Compare times, displayCode() or not

Needs:
Redo async test events - affects RI project

Questions:
1) Can I reasonable measure recalcstyle time by comparing time it takes a function a run before and after?

*/

var suites = [
  {
    name: "Recalculate Styles",
    code: "somanystyles,solittletime",
    tests: [
      {
        func: "testCompareFunctionRunTimes",
        async: true,
        params: [
          {
            func: styleSwapper, // should already be defined globally.
            initRun: 2,   // how many times to run the function on init to collect data
            timeFactorDiff: 2  // multiplier for time drop. 2 refers to a 2x drop in runtime
          }
        ],
        desc: "Function runtime is halved"
      }
    ]
  }
]

var graderProperties = {
  suites: suites
}