import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
    vus: 5,
    duration: "30s",

    thresholds: {
        http_req_duration: ["p(95)<1000"],
        http_req_failed: ["rate<0.05"]
    }
};

const API_KEY = __ENV.REQRES_API_KEY;

export default function () {

    const response = http.get(
        "https://reqres.in/api/users?page=2",
        {
            headers: {
                "x-api-key": API_KEY
            }
        }
    );

    let body = {};

    try {
        body = response.json();
    } catch (e) {
        body = {};
    }

    check(response, {
        "status is 200": (r) => r.status === 200,
        "not rate limited": (r) => r.status !== 429,
        "response contains data array": () =>
            Array.isArray(body.data),
        "contains users": () =>
            Array.isArray(body.data) &&
            body.data.length > 0
    });

    if (!Array.isArray(body.data)) {
        console.log(
            `Unexpected response: status=${response.status} body=${response.body}`
        );
    }

    sleep(1);
}