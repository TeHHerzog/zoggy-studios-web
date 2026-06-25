# Domain Mapping

## Studio Site

```text
games.herzogit.com
-> IONOS webspace
-> /games/
-> upload contents of dist/studio/
```

## Dark Fantasy Site

```text
darkfantasy.herzogit.com
-> IONOS webspace
-> /darkfantasy/
-> upload contents of dist/darkfantasy/
```

## Upload Rule

Upload the contents of each output directory, not the parent `dist` directory itself.

Correct:

```text
dist/studio/index.html      -> /games/index.html
dist/darkfantasy/index.html -> /darkfantasy/index.html
```

Incorrect:

```text
dist/studio/      -> /games/studio/
dist/darkfantasy/ -> /darkfantasy/darkfantasy/
```

## Unverified Remote Checks

Local builds cannot prove DNS, HTTPS, IONOS directory mapping, remote directory listing behavior, or remote 404 behavior. Those checks must be performed manually after upload.
