import {useState} from "react";

import {axiosService} from "../services";


const UrlForm = () => {
    const [url, setUrl] = useState('');
    const [res, setRes] = useState('')

    const getUrl = async () => {
        const {url_result} = await axiosService.post('/create_short', {url}).then(({data}) => data);
        setRes(url_result)
    }

    return (
        <div>
            <input type="text" onChange={(e) => setUrl(e.target.value)} value={url}/>
            <button onClick={getUrl} disabled={!url}>get</button>
            {res && <div>{res} <hr/> </div>}
        </div>
    );
};

export {UrlForm};