GrapesJS Builder
################

The GrapesJS Builder doesn't require any special HTML syntax to edit content in the Builder. However, for Emails, it supports the :xref:`MJML email framework` to create responsive emails.

.. code-block:: html

    <mjml>
      <mj-body>
        <mj-raw>
          <!-- Company Header -->
        </mj-raw>
        <mj-section background-color="#f0f0f0">
          <mj-column>
            <mj-text font-style="bold" font-size="24px" color="#6f6f6f">My Company</mj-text>
          </mj-column>
        </mj-section>
        <mj-raw>
          <!-- Confirm  text -->
        </mj-raw>
        <mj-section background-color="#fafafa">
          <mj-column width="400px">
            <mj-text font-style="bold" font-size="22px" font-family="Helvetica Neue" color="#626262">Please confirm your subscription!</mj-text>
            <mj-button background-color="#F45E43" font-style="bold" href="#">Yes, subscribe me to the list</mj-button>
            <mj-text color="#525252" font-size="16" line-height="1.5">If you received this email by mistake, simply delete it. You won't be subscribed if you don't click the confirmation link above.<br/><br/>For questions about this list, please contact:
    email@example.com</mj-text>
          </mj-column>
        </mj-section>
            <mj-raw>
          <!-- Confirm  text -->
        </mj-raw>
            <mj-section background-color="#fafafa">
          <mj-column width="400px">
            <mj-text color="#525252" line-height="1.2">
              <p>Company Name<br/>111 Amazing Street<br/>
                Beautiful City</p></mj-text>

          </mj-column>
        </mj-section>
      </mj-body>
    </mjml>