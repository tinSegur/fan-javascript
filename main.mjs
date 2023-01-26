import {precip_geo, precip_topo} from "./module/parse_netcdf_test.mjs";

const levels = precip_geo[0].map(d => d.value)
const features = precip_topo[0].objects.map(objt => ChartGeo.topojson.feature(precip_topo[0], objt))

const chart = new Chart(document.getElementById('canvas').getContext('2d'), {
    type: 'choropleth',
    data: {
        labels: precip_topo.objects.keys,
        datasets: [
            {
                label: 'Levels',
                outline: level,
                data: features.map((f) => ({
                    feature: f,
                    value: 1,
                })),
            },
        ],
    },
    options: {
        showOutline: false,
        showGraticule: false,
        plugins: {
            legend: {
                display: false,
            },
        },
        scales: {
            projection: {
                axis: 'x',
                projection: 'equalEarth',
                padding: 10,
            },
        },
    },
})


