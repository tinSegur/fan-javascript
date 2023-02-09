import * as fs from 'fs'
import * as d3c from 'd3-contour'

function map_coords(val, ran1, ran2){
    //maps a value val1 from the range ran1 linearly onto the range ran2
    var slope = (ran2[1] - ran2[0])/(ran1[1] - ran1[0])
    return (val-ran1[0])*slope+ran2[0]
}

function convert_coords_multipolygon(multi, xrange1, xrange2, yrange1, yrange2){
    var ret_copy = multi
    for (let i = 0; i < ret_copy.coordinates.length; i++){
        for (let k = 0; k < ret_copy.coordinates[i].length; k++){
            ret_copy.coordinates[i][k] = ret_copy.coordinates[i][k].map((vl) => [
                map_coords(vl[0], xrange1, xrange2),
                map_coords(vl[1], yrange1, yrange2)])
        }
    }
    return ret_copy
}

function generate_contours(vardir, varname, threshes){
    let meta_json = JSON.parse(fs.readFileSync(vardir + '/' + varname + '_meta.json', 'utf8'))
    let json_arr = fs.readdirSync(vardir + '/' + varname +'_data/').map((dir) => JSON.parse(fs.readFileSync(vardir + '/'+varname+'_data/' + dir, 'utf8').replace(/\bNaN\b/g, "null")))

    const lat_size = json_arr[0].lat.length
    const lon_size = json_arr[0].lon.length


    const cntgen = d3c.contours()
        .thresholds(threshes)
        .size([lon_size, lat_size])

    let data_arr = json_arr.map((json) => json[varname])
    let cnt_arr = data_arr.map((data) => cntgen(data.flat(4)))
    cnt_arr = cnt_arr.map((conts) => (conts.map((geoj) => (convert_coords_multipolygon(geoj,
        [0, lon_size],
        [meta_json['lon_interval']['start'], meta_json['lon_interval']['end']],
        [0, lat_size],
        [meta_json['lat_interval']['start'], meta_json['lat_interval']['end']]
        )))))

    for (let i = 0; i<cnt_arr.length; i++){
        let geo = cnt_arr[i]
        fs.writeFile(vardir + '/' + varname + '_geo/' + varname + '-geo-' + json_arr[i].year + '.json', JSON.stringify(geo), (error) =>{
            if (error) throw error
        })

    }

}

const sst_threshes = Array.from(new Array(6), (x, i) => i*6)
console.log(sst_threshes)
generate_contours("C:/Users/marti/Documents/Practica FAN/fan-javascript/vis_data/sst", 'sst', sst_threshes)

const tp_threshes = Array.from(new Array(6), (x, i) => i*(6/1000))
console.log(tp_threshes)
generate_contours("C:/Users/marti/Documents/Practica FAN/fan-javascript/vis_data/tp", 'tp', tp_threshes)

const u_threshes = Array.from(new Array(6), (x, i) => (i*(9/6)))
console.log(u_threshes)
generate_contours("C:/Users/marti/Documents/Practica FAN/fan-javascript/vis_data/u", 'u', u_threshes)

const v_threshes = Array.from(new Array(6), (x, i) => (-3 + i))
console.log(v_threshes)
generate_contours("C:/Users/marti/Documents/Practica FAN/fan-javascript/vis_data/v", 'v', v_threshes)

