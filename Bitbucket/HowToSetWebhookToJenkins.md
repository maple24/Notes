# How to set webhook to Jenkins

## Jenkins configuration

### Credentials

1. Bitbucket HTTP token (username with password)
   The password is HTTP-access-token of **your Bitbucket Account**. (Not your repo!!)
   ![bitubcket http token](assets/bitbucket_http_token.png.png)

2. Personal access token
   This token is specially used for bitbucket server instance. This token is retrieved from your repo HTTP-access-token.
   ![personal access token](assets/bitbucket_admin_token.png)

### Bitbucket server integration

![bitbucket server integration](assets/Bitbucket_server_integration.png)

### Bitbucket server

![bitbucket server 1](assets/Bitbucket_server_1.png)
![bitbucket server 2](assets/Bitbucket_server_2.png)

### Pipeline configuration

1. Pipeline script should come from scm
   ![scm_1](assets/pipeline_1.png)
   ![scm_2](assets/pipeline_2.png)
   ![trigger](assets/pipeline_3.png)

## Bitbucket configuration

### hooks

![hooks 1](assets/hooks_1.png)
Turn on the builds wedget.
![hooks 2](assets/hooks_2.png)

### webhooks

1. link webhook in add-on
   ![webhook add-on](assets/webhooks_1.png)

2. the webhook in workflow will be linked automatically
   ![webhook link](assets/webhooks_2.png)

### builds

![builds](assets/builds.png)
