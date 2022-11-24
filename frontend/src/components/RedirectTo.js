import {useNavigate, useParams} from "react-router-dom";

import {axiosService} from "../services";

const RedirectTo = () => {
    const {value} = useParams();
    const navigate = useNavigate();

    (async () => {
        const {result} = await axiosService.get(`/redirect/${value}`).then(({data}) => data);
        result ? window.location.replace(result) : navigate('/')
    })()

    return <div>LOADING ...</div>
};

export {RedirectTo};