import {Route, Routes} from "react-router-dom";

import {RedirectTo} from "./components";
import {HomePage} from "./pages";

function App() {
    return (
        <Routes>
            <Route path={''} element={<HomePage/>}/>
            <Route path={':value'} element={<RedirectTo/>}/>
        </Routes>
    );
}

export {App};