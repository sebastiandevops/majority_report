#!/usr/bin/node
fetch('https://raw.githubusercontent.com/sebasvalencia726/majority_report/master/data.csv')
  .then(function (response) {
    return response.text();
  })
  .then(function (text) {
    csvToSeries(text);
  })
  .catch(function (error) {
    console.log(error);
  });

function csvToSeries (text) {
  const dataAsJson = JSC.csv2Json (text);
  console.log(dataAsJson);
}
