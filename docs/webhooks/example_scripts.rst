Webhook example scripts
==========================================================

PHP
---

.. code-block:: php

    <?php
    // webhookTest.php

    declare(strict_types=1);

    /**
     * A helper class to log and get the Mautic webhook request
     */
    class webhookTest {
        /**
         * Log a message to a file
         */
        public function log(string $message, string $type = 'info'): void
        {
            $prefix = 'webhookLog_';
            $file = $type . '.log';
            $date = new DateTime();

            error_log($date->format('Y-m-d H:i:s') . ' ' . $message . "\n\n", 3, $prefix . $file);
        }

        /**
         * Get the request JSON object and log the request
         */
        public function getRequest(): string
        {
            $rawData = file_get_contents("php://input");

            $this->log($rawData, 'request');

            return $rawData;
        }
    }

    $secret = 'mySuperWebhookSecretKey';
    $webhook = new webhookTest;
    $rawData = $webhook->getRequest();

    // optional signature verification
    $headers = getallheaders();
    $receivedSignature = $headers['Webhook-Signature'];
    $computedSignature = base64_encode(hash_hmac('sha256', $rawData, $secret, true));

    if ($receivedSignature === $computedSignature) {
        $webhook->log('Webhook authenticity verification OK', 'request');
    } else {
        $webhook->log('Webhook not authentic!', 'request');
    }

    // @todo Process the $requestData as needed
    $requestData = json_decode($rawData);

    if (isset($requestData['mautic.lead_post_save_new'])) {
        foreach ($requestData['mautic.lead_post_save_new'] as $contact) {
            // do something with the newly identified Contacts
        }
    }

Node.js
--------

.. code-block:: javascript

    'use strict';

    const express = require('express');
    const crypto = require('crypto');
    const app = express();
    const port = 3000;
    const SECRET = 'mySecret';

    // save raw body
    app.use ((req, res, next) => {
        let data = '';
        req.setEncoding('utf8');

        req.on('data', chunk => data += chunk);
        req.on('end', () => {
            req.body = data;
            return next();
        });
    });

    app.post('/webhook', (req, res) => {

        // optional signature verification
        const receivedSignature = req.headers['webhook-signature'];
        console.log('Received signature (in header):', receivedSignature);

        const computedSignature = crypto.createHmac('sha256', SECRET).update(req.body).digest('base64');
        console.log('Computed signature (from body):', computedSignature);

        if (receivedSignature === computedSignature) {
            console.log('Webhook authenticity verification OK');
        } else {
            console.log('Webhook not authentic!');
        }

        // TODO: process body
        const body = JSON.parse(req.body);

        if (body["mautic.lead_post_save_new"].length) {
            // do something with the array of newly identified Contacts
        }

        res.send();
    });

    app.listen(port, () => console.log(`App listening on port ${port}!`));
