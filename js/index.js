#!/usr/bin/node
'use strict';

fetch('https://data.cdc.gov/resource/w9j2-ggv5.csv')
  .then(function (response) {
    return response.text();
  })
  .then(function (text) {
    let series = csvToSeries(text);
    renderChart(series);
  })
  .catch(function (error) {
    console.log(error);
  });

function csvToSeries (text) {
  const lifeExp = 'average_life_expectancy';
  let dataAsJson = JSC.csv2Json(text);
  let white = [];
  let black = [];
  dataAsJson.forEach(function (row) {
    if (row.sex === 'Both Sexes') {
      if (row.race === 'Black') {
        black.push({ x: row.year, y: row[lifeExp] });
      } else if (row.race === 'White') {
        white.push({ x: row.year, y: row[lifeExp] });
      }
    }
  });
  return [
    { name: 'Black', points: black },
    { name: 'White', points: white },
  ];
}

function renderChart (series) {
  JSC.Chart('chartDiv', {
    title_label_text: 'Life Expectancy in the United States',
    annotations: [{
      label_text: 'Source: National Center for Health Statistics',
      position: 'bottom left'
    }],
    legend_visible: false,
    xAxis_crosshair_enabled: true,
    defaultSeries_lastPoint_label_text: '<b>%seriesName</b>',
    defaultPoint_tooltip: '%seriesName <b>%yValue</b> years',
    series: series
  });
}
