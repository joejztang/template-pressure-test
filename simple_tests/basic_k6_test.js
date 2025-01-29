import http from 'k6/http';
import { describe } from 'https://jslib.k6.io/expect/0.0.4/index.js';
import { check, sleep } from 'k6';
export default function () {
    describe('Basic k6 test', () => {
        // TODO: fill in testable endpoint for your service.
        // let res = http.get('http://poetry-project:8000');
        let res = http.get('https://test.k6.io');
        check(res, {
            'is status 200': (r) => r.status === 200
        });
        sleep(1);
    });
}