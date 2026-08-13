# RA Flooring — Website

Site estático moderno da **RA Contractor Flooring Inc.** (Davenport, FL), reconstruído a partir do antigo WordPress/Elementor de raflooringusa.com.

## Estrutura

- `*.html` — 11 páginas estáticas (home, about, services, gallery, contact, kitchen/bathroom remodeling, painting, thank-you, privacy, terms)
- `assets/css/style.css` — folha de estilo única (design system: laranja #F15522 + grafite)
- `assets/js/main.js` — navegação mobile, contadores animados, reveal on scroll, slider before/after, player de vídeos
- `assets/img` / `assets/video` — mídia original migrada do WordPress
- `build.py` — gerador das páginas (header/footer compartilhados). Edite e rode `python build.py` para regenerar os HTML.

## Rodando localmente

```bash
python -m http.server 8080 --directory .
```

Depois abra http://localhost:8080

## Formulário de contato

O formulário em `contact.html` envia via [formsubmit.co](https://formsubmit.co) para o e-mail da empresa e redireciona para `thank-you.html`. No primeiro envio em produção, o formsubmit manda um e-mail de confirmação que precisa ser aprovado uma única vez.

## Deploy

É um site 100% estático — qualquer host serve (GitHub Pages, Netlify, Vercel, ou o próprio servidor nginx atual apontando para esta pasta).
