//! The Nation and project links (shown in Help, About, the start screen, the CLI and MCP). The
//! names keep their upstream spelling (`DISCORD` is the Nation, `APPS` the Atelier suite) so callers
//! and the `app.links` keys stay the same.

/// The Aetherion Nation.
pub const DISCORD: &str = "https://www.aetherionnnation.com";
/// The Nation's home page.
pub const WEBSITE: &str = "https://www.aetherionnnation.com/";
/// Atelier, the Nation's creative suite.
pub const APPS: &str = "https://www.aetherionnnation.com/atelier";
/// Atelier Podium's page on the Nation site.
pub const APP_PAGE: &str = "https://www.aetherionnnation.com/atelier/podium";
/// Atelier Podium's source repository.
pub const GITHUB: &str = "https://github.com/Aetherion-Nation-Builders/atelier-podium";
pub const ISSUES: &str = "https://github.com/Aetherion-Nation-Builders/atelier-podium/issues";

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn links_follow_the_atelier_scheme() {
        assert!(WEBSITE.starts_with(DISCORD) && APPS.starts_with(DISCORD));
        assert_eq!(APP_PAGE, format!("{APPS}/podium"));
        assert!(GITHUB.ends_with("/atelier-podium") && ISSUES.starts_with(GITHUB));
    }
}
