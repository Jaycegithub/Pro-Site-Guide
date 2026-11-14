You are helping me set up Facebook's official Graph API so a publishing tool can post to my Facebook Page "Pro Site Guide" (Page ID 1511889748663901). I'm logged in to Facebook in this Chrome browser and I'm an admin of that Page.

GOAL
Create a Meta developer app and generate a long-lived ("never expires") PAGE access token for the Pro Site Guide Page, with permission to publish and schedule posts.

RULES
- Work only on developers.facebook.com and the Facebook login/permission dialogs it opens.
- Don't change any Page settings, post anything, add payment methods, or submit anything for App Review or Business Verification. The app stays in Development mode (that's enough, because I'm the app admin and a Page admin).
- SECRETS: never copy, paste or type an access token, App Secret or password into any chat, document, form or other website, and don't repeat them in your messages to me. When a token appears on screen, just tell me where it is and I'll copy it myself.
- Before any final "Create", "Continue as…" or permission-confirm button, tell me what you're about to confirm and wait for my OK.
- If you see a login, two-factor, security check, "verify your account" or any screen you're unsure about, stop and ask me.

STEP 1: Create the app
1. Go to https://developers.facebook.com/apps and click "Create app". If asked to register as a developer first, stop and let me do that, then continue.
2. App name: ProSiteGuide Publisher. Contact email: my Facebook account email (ask me if it isn't pre-filled).
3. Use case: choose the one for managing a Facebook Page, usually "Manage everything on your Page" (or "Other" → app type "Business" if that's what's offered).
4. Business portfolio: skip or choose "I don't want to connect a business portfolio yet", unless it's required. If it is, ask me.
5. Finish creating the app and tell me the App ID shown on the dashboard. (The App ID isn't secret.)

STEP 2: Add the permissions
In the app's use case settings ("Customize" the Page use case, or Permissions), make sure these are added/ready for testing:
- pages_show_list
- pages_read_engagement
- pages_manage_posts
If "business_management" is required by the use case, add it too. Don't request anything else.

STEP 3: Generate a user token in Graph API Explorer
1. Go to https://developers.facebook.com/tools/explorer/
2. In "Meta App", select "ProSiteGuide Publisher".
3. In "User or Page", choose "Get User Access Token".
4. In Permissions, add: pages_show_list, pages_read_engagement, pages_manage_posts.
5. Click "Generate Access Token". In the Facebook dialog, choose to opt in to the Page "Pro Site Guide" (only that Page), allow all three permissions, and confirm. Ask me before the final confirm.

STEP 4: Extend the user token (no App Secret needed)
1. Copy the token from the Explorer's "Access Token" field into the Access Token Debugger: https://developers.facebook.com/tools/debug/accesstoken/. Debugging inside Meta's own tool is allowed; don't paste it anywhere else.
2. Click "Debug", then click "Extend Access Token" at the bottom. Facebook will show a new long-lived user token (about 60 days).
3. Back in Graph API Explorer, replace the Access Token field with that long-lived token.

STEP 5: Get the Page access token
1. In Graph API Explorer, keep method GET and enter this query:
   me/accounts?fields=name,id,access_token,tasks
2. Click "Submit". Find the entry with id 1511889748663901 (name "Pro Site Guide"). Check that "tasks" includes "CREATE_CONTENT".
3. Its "access_token" value is the Page access token. Don't copy it anywhere.
4. To verify it, open https://developers.facebook.com/tools/debug/accesstoken/ in a new tab, and let me paste the Page token there myself. Then tell me what "Type" (should be Page), "Page ID" (1511889748663901), "Expires" (should be "Never") and "Scopes" show.

WHEN FINISHED
Report back with: the App ID, the app mode (Development), the permissions granted, and the Debugger results for the Page token (Type, Page ID, Expires, Scopes). Remind me NOT to paste the token into any chat. I'll enter it into Claude Code's secure credential form for graph.facebook.com.
