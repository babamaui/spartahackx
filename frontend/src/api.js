import axios from "axios";

export const query = (question) => {
    const response = axios.get("http://localhost:8080/query", {question});
    console.log(response.data);
    return response.data;
}

export const ingest = (filename) => {
    const response = axios.post("/ingest", {filename});
    console.log(response.data);
    return response.data;
}
