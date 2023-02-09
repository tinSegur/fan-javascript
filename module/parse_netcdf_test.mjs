import * as tpj from "topojson-server"
import * as cdf from "netcdfjs"
import * as d3c from "d3-contour"
import * as d3g from "d3-geo"
import * as fs from "fs"

import * as chg from "chartjs-chart-geo"

const data = fs.readFileSync("../data/precipitacion_DJF_2000_2020_Patagonia.nc");
var reader = new cdf.NetCDFReader(data);

var latlen = reader.getDataVariable("latitude").length
var lonlen = reader.getDataVariable("longitude").length
var precip_raw = reader.getDataVariable("tp").map(pnt => (pnt*5.486614236666784e-7 + 0.017977440207862384)*1000)
precip_raw.splice(precip_raw.length-1, 1)
//var info = reader.header.variables[3]
var info = reader.getDataVariable("time").map(dt => new Date(dt*1000*60*60-1000*60*60*24*365*70))
//console.log(info)

var precip_data = new Array()
for (let i = 0; i<63; i++){
    precip_data.push(precip_raw.splice(0, 101*161))
}
console.log(precip_data)


//var cntgen = d3c.contours().size([lonlen, latlen])
//console.log(cntgen)

//var precip_geo = precip_data.map(dt => cntgen(dt))
//console.log(precip_geo)

//var precip_topo = precip_geo.map(g => tpj.topology(g))
//console.log(precip_topo)

//for (let i = 0; i<63; i++){
//    fs.writeFile("../data/tp_" + info[i].toISOString().slice(0, 10) + "_topo.json", JSON.stringify(precip_topo[i]), (error) =>{
//        if (error) throw error
//    })
//    fs.writeFile("../data/tp_" + info[i].toISOString().slice(0, 10) + "_geo.json", JSON.stringify(precip_geo[i]), (error) =>{
//        if (error) throw error
//    })
//}

//console.log(precip_topo[0])
//console.log(precip_geo[0])
//console.log(precip_topo[0].objects)
//console.log(pchg.topojson.feature(precip_topo[0], precip_topo[0].objects))
