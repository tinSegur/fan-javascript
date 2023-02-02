import * as fs from 'fs'
import * as d3c from 'd3-contour'



function generate_contours(vardir, varname, threshes){
    let meta_json = JSON.parse(fs.readFileSync(vardir + '/' + varname + '_meta.json', 'utf8'))
    let json_arr = fs.readdirSync(vardir + '/' + varname +'_data/').map((dir) => JSON.parse(fs.readFileSync(vardir + '/'+varname+'_data/' + dir, 'utf8').replace(/\bNaN\b/g, "null")))
    console.log(json_arr)

    const lat_size = json_arr[0].lat.length
    const lon_size = json_arr[0].lon.length


    const cntgen = d3c.contours()
        .thresholds(threshes)
        .size([lon_size, lat_size])

    let data_arr = json_arr.map((json) => json.sst)
    let cnt_arr = data_arr.map((data) => cntgen(data.flat(4)))

    for (let i = 0; i<cnt_arr.length; i++){
        let geo = cnt_arr[i]
        fs.writeFile(vardir + '/' + varname + '_geo/' + varname + '-geo-' + json_arr[i].year + '.json', JSON.stringify(geo), (error) =>{
            if (error) throw error
        })

    }



}

const threshes = Array.from(new Array(6), (x, i) => i*6)
console.log(threshes)
generate_contours("C:/Users/marti/Documents/Practica FAN/fan-javascript/vis_data/sst", 'sst', threshes)