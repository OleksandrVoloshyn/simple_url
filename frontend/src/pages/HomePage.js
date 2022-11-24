import {useState} from "react";

import {axiosService} from "../services";
import {UrlForm} from "../components";

const HomePage = () => {
    const [rates, setRates] = useState(null);

    const getTop = async () => {
        const {top_list} = await axiosService.get('/rates', {params: {top: 10}}).then(({data}) => data);
        setRates(top_list)
    }

    return (
        <div>
            <span>MainPage</span>
            <button onClick={getTop}>Get top 10</button>
            <UrlForm/>

            {rates && rates.map(item => <div key={item['id']}>
                <div>url -- <b>{item['base']}</b></div>
                <div>clicks -- {item['clicks']}</div>
                <br/>
            </div>)}
        </div>
    );
};

export {HomePage};