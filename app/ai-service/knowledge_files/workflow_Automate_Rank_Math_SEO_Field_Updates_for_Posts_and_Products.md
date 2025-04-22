# Automate Rank Math SEO Field Updates for Posts and Products

**[View Template](https://n8n.io/workflows/2836-/)**  **Published Date:** 02/02/2025  **Created By:** phil  **Categories:** `Development` `Core Nodes`  

## Template Description

This workflow automates the process of updating important Rank Math SEO fields (SEO Title, Description, and Canonical URL) directly via n8n. 

By leveraging a custom WordPress plugin that extends the WordPress REST API, this workflow ensures that you can programmatically manage SEO metadata for your posts and WooCommerce products efficiently.

How it works:
Sends a POST request to a custom API endpoint exposed by the Rank Math plugin.
Updates SEO Title, Description, and Canonical URL fields for a specified post or product.

Setup steps:
Install and activate the Rank Math API Manager Extended plugin on WordPress.
Provide the post or product ID you want to update in the workflow.
Run the workflow to update the metadata automatically.

Benefits:
Full automation of SEO optimizations.
Works for both standard posts and WooCommerce products.
Simplifies large-scale SEO management tasks.

To understand exactly how to use it in detail, check out my comprehensive documentation here.





Rank Math API Manager Extended plugin on WordPress

&lt;?php
/**
 Plugin Name: Rank Math API Manager Extended v1.3
 Description: Manages the update of Rank Math metadata (SEO Title, SEO Description, Canonical URL) via the REST API for WordPress posts and WooCommerce products.
 Version: 1.3
 Author: Phil - https://inforeole.fr
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

class Rank_Math_API_Manager_Extended {
    public function __construct() {
        add_action('rest_api_init', [$this, 'register_meta_fields']);
        add_action('rest_api_init', [$this, 'register_api_routes']);
    }

    /**
     Registers the Rank Math meta fields in the REST API for posts and products (if WooCommerce is active).
     */
    public function register_meta_fields() {
        $meta_fields = [
            'rank_math_title'         =&gt; 'SEO Title',
            'rank_math_description'   =&gt; 'SEO Description',
            'rank_math_canonical_url' =&gt; 'Canonical URL'
        ];

        // Register meta for posts by default.
        $post_types = ['post'];

        // If WooCommerce is active, add the 'product' post type.
        if ( class_exists('WooCommerce') ) {
            $post_types[] = 'product';
        }

        foreach ( $post_types as $post_type ) {
            foreach ( $meta_fields as $key =&gt; $description ) {
                register_post_meta( $post_type, $key, [
                    'show_in_rest'   =&gt; true,
                    'single'         =&gt; true,
                    'type'           =&gt; 'string',
                    'auth_callback'  =&gt; [$this, 'check_update_permission'],
                    'description'    =&gt; $description,
                ] );
            }
        }
    }

    /**
     Registers the REST API route to update Rank Math meta fields.
     */
    public function register_api_routes() {
        register_rest_route( 'rank-math-api/v1', '/update-meta', [
            'methods'             =&gt; 'POST',
            'callback'            =&gt; [$this, 'update_rank_math_meta'],
            'permission_callback' =&gt; [$this, 'check_update_permission'],
            'args'                =&gt; [
                'post_id' =&gt; [
                    'required'          =&gt; true,
                    'validate_callback' =&gt; function( $param ) {
                        return is_numeric( $param ) && get_post( $param );
                    }
                ],
                'rank_math_title' =&gt; [
                    'type'              =&gt; 'string',
                    'sanitize_callback' =&gt; 'sanitize_text_field',
                ],
                'rank_math_description' =&gt; [
                    'type'              =&gt; 'string',
                    'sanitize_callback' =&gt; 'sanitize_text_field',
                ],
                'rank_math_canonical_url' =&gt; [
                    'type'              =&gt; 'string',
                    'sanitize_callback' =&gt; 'esc_url_raw',
                ],
            ],
        ] );
    }

    /**
     Updates the Rank Math meta fields via the REST API.
     */
    public function update_rank_math_meta( WP_REST_Request $request ) {
        $post_id = $request-&gt;get_param( 'post_id' );
        $fields  = ['rank_math_title', 'rank_math_description', 'rank_math_canonical_url'];
        $result  = [];

        foreach ( $fields as $field ) {
            $value = $request-&gt;get_param( $field );
            if ( $value !== null ) {
                $update_result = update_post_meta( $post_id, $field, $value );
                $result[ $field ] = $update_result ? 'updated' : 'failed';
            }
        }

        if ( empty( $result ) ) {
            return new WP_Error( 'no_update', 'No metadata was updated', ['status' =&gt; 400] );
        }

        return new WP_REST_Response( $result, 200 );
    }

    /**
     Checks if the current user has permission to update the meta fields.
     */
    public function check_update_permission() {
        return current_user_can( 'edit_posts' );
    }
}

new Rank_Math_API_Manager_Extended();


.

Phil | Inforeole

## Template JSON

```
{
  "meta": {
    "instanceId": "c911aed9995230b93fd0d9bc41c258d697c2fe97a3bab8c02baf85963eeda618",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "83c6d7e3-ae2e-4576-8bc6-1e1a7b553fca",
      "name": "Settings",
      "type": "n8n-nodes-base.set",
      "position": [
        260,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "080b234c-a753-409d-9d2d-3322678a01f2",
              "name": "woocommerce url",
              "type": "string",
              "value": "https://mydom.com/"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "7018ae65-bb9d-4bac-8746-01193cb0e523",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        0,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "223ed34b-3e26-406c-a5a5-34f8408e3fe6",
      "name": "HTTP Request - Update Rank Math Meta",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        500,
        0
      ],
      "parameters": {
        "url": "={{ $('Settings').item.json[\"woocommerce url\"] }}wp-json/rank-math-api/v1/update-meta",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "post_id",
              "value": "246"
            },
            {
              "name": "rank_math_title",
              "value": "Demo SEO Title"
            },
            {
              "name": "rank_math_description",
              "value": "Demo SEO Description"
            },
            {
              "name": "rank_math_canonical_url",
              "value": "https://example.com/demo-product"
            }
          ]
        },
        "nodeCredentialType": "wordpressApi"
      },
      "credentials": {
        "wordpressApi": {
          "id": "6rPlJdCaIXaVciGM",
          "name": "Wordpress account"
        },
        "wooCommerceApi": {
          "id": "klGFZkgHrRfC8BVg",
          "name": "WooCommerce account"
        }
      },
      "retryOnFail": true,
      "typeVersion": 4.2
    }
  ],
  "pinData": {},
  "connections": {
    "Settings": {
      "main": [
        [
          {
            "node": "HTTP Request - Update Rank Math Meta",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \u2018Test workflow\u2019": {
      "main": [
        [
          {
            "node": "Settings",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
