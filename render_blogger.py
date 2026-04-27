import re

def render(filepath, output_path):
    with open(filepath, 'r') as f:
        content = f.read()

    # Simple replacements for preview
    content = content.replace('<b:skin><![CDATA[', '<style>')
    content = content.replace(']]></b:skin>', '</style>')
    content = content.replace('<script>//<![CDATA[', '<script>')
    content = content.replace('//]]></script>', '</script>')

    # Blogger Variables mapping
    content = content.replace('$(primary.color)', '#6366f1')
    content = content.replace('$(secondary.color)', '#a855f7')
    content = content.replace('$(accent.color)', '#f43f5e')
    content = content.replace('$(bg.color)', '#0f172a')
    content = content.replace('$(surface.color)', '#1e293b')
    content = content.replace('$(text.color)', '#f8fafc')
    content = content.replace('$(muted.text.color)', '#94a3b8')
    content = content.replace('$(button.bg)', '#6366f1')
    content = content.replace('$(button.text)', '#ffffff')
    content = content.replace('$(button.radius)', '50px')
    content = content.replace('$(card.bg)', '#1e293b')
    content = content.replace('$(card.shadow)', '0 10px 15px -3px rgba(0, 0, 0, 0.1)')
    content = content.replace('$(card.radius)', '24px')
    content = content.replace('$(input.bg)', '#1e293b')
    content = content.replace('$(input.border)', '#334155')
    content = content.replace('$(input.text)', '#f8fafc')
    content = content.replace('$(input.focus.border)', '#6366f1')

    # Remove Blogger specific tags but keep content
    content = re.sub(r'<b:section[^>]*>', '<div>', content)
    content = content.replace('</b:section>', '</div>')

    # Handle Widgets (simplified)
    content = re.sub(r'<b:widget[^>]*>', '<div>', content)
    content = content.replace('</b:widget>', '</div>')

    # Data tags
    content = content.replace('<data:view.title.escaped/>', 'Antinna - UI/UX Perfected')
    content = content.replace('<data:blog.url.jsonEscaped/>', '#')
    content = content.replace('<data:blog.url/>', '#')
    content = content.replace('<data:blog.title/>', 'Antinna')
    content = content.replace('<data:blog.metaDescription/>', 'Premium Blogger Theme')

    # Conditional tags
    content = re.sub(r'<b:if[^>]*>', '', content)
    content = content.replace('</b:if>', '')

    with open(output_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    render('antinna-landing-page.xml', 'preview.html')
