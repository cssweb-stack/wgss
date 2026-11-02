# WGSS demonstration

14 pages using the shared CSS website foundation. Each has an H1, subtitle, larger introduction, and six body paragraphs. Department-specific academic material is placeholder text. The Contact page uses the supplied department contact details; the privacy page describes the demonstration.

## Install the shared update FIRST

This package includes css-shared/src/_includes/components/hero.njk and hero-attribution.njk. Replace those two files in your LOCAL css-shared folder. These add optional hero flags and keep the existing defaults for GEO and SOC. In GitHub Desktop select css-shared, enter “Support optional hero labels and credits”, Commit to main, then Push origin. The shared update must be online before WGSS deploys.

## Install WGSS on your Mac

In GitHub Desktop choose File > Clone Repository > URL, enter https://github.com/cssweb-stack/wgss.git, and clone beside geo, soc and css-shared. Copy everything INSIDE this wgss folder into the new clone, including .github and .gitignore. Keep the clone’s .git folder. Do not nest wgss inside wgss.

In VS Code choose File > Add Folder to Workspace, select wgss, then right-click wgss > Open in Integrated Terminal. Run:

```
npm ci
npm run dev
```

WGSS uses port 8083 so other previews can remain running. No shared:adopt step is needed for a new repository.

## Publish

On the GitHub website choose cssweb-stack/wgss > Settings > Pages > Build and deployment > Source > GitHub Actions. In GitHub Desktop select wgss, enter “Add WGSS shared-foundation demonstration”, Commit to main, then Publish branch or Push origin. Open the repository’s Actions tab and wait for Build and publish WGSS to turn green. Published URL: https://cssweb-stack.github.io/wgss/.

## Where to edit

src/_data/site.json: unit name, search, logo, address, phone, email, social links, privacy/webmaster links, and hero feature flags. socialLinks is empty. The menu label supplied as About SOC was corrected to About WGSS.

src/_data/navigation.json: navigation and URLs.

src/_data/heroes.json: assignments cycle hero-01.webp, hero-02.webp, hero-03.webp in navigation order, starting at Home and ending at Privacy. The three uploaded image files are copied unchanged to src/_media/heros/ (the existing shared folder spelling).

site.hero.decorative=true hides the decorative hero region from assistive technology. showLocation=false omits location text. showAttribution=false omits the imagery bar. No location or attribution is invented. Shared sizing, responsive behavior, fade, and patterned treatment remain intact. Grayscale is zero to retain the uploaded image colors.

src/_media/unit/wgss-logo-white.svg: optimized vector logo. Original 500 by 320 viewBox and all shape geometry preserved.

src/wgss.css: local overrides. The current shared base loads geo.css; Eleventy publishes wgss.css under that compatibility output name. No GEO styles are duplicated.

Shared copies generated inside src are ignored by Git. Maintain their authoritative files in css-shared.
