import axios from "axios";

const baseURL = process.env.REACT_APP_API;
const axiosService = axios.create({baseURL});

export {axiosService}