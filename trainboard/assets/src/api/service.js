import axios from 'axios'


function retFunc(response) {
    let status_code = response.status;
    if (status_code == 200){
        return response.data;
    }else {
        return response;
    }
}

function setParams(url, data) {
        let dataStr = ''; //数据拼接字符串
		Object.keys(data).forEach(key => {
            if (data[key]) {
                dataStr += key + '=' + data[key] + '&';
            }
		})
		if (dataStr !== '') {
			dataStr = dataStr.substr(0, dataStr.lastIndexOf('&'));
			url = url + '?' + dataStr;
		}
        return url;
}

export default async(url = '', data = {}, type = 'GET') => {
    type = type.toUpperCase();
	if (type == 'GET') {
		url = setParams(url, data);
        const response = await axios.get(url);
        return retFunc(response);
	}else if (type == 'POST'){
        const response = await axios.post(url, data);
        return retFunc(response);
    } else if (type == "PUT") {
        const response = await axios.put(url, data);
        return retFunc(response);
    } else if (type == "DELETE") {
        url = setParams(url, data);
        const response = await axios.delete(url, data);
        return retFunc(response);
    }
}
