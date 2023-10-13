let data, spec;

// Fetch the data
fetch('./data.json')
  .then(response => response.json())
  .then(d => {
    data = d;
    return fetch('./vega_lite.json');
  })
  .then(response => response.json())
  .then(specJson => {
    spec = specJson;
    // Add the fetched data to the spec
    spec.data = { values: data };
    // Embed the visualization
    vegaEmbed('#vis1', spec, { "actions": false });
  })
  .catch(error => {
    console.error("Error loading JSON files:", error);
  });
