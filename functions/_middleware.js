export async function onRequest(context) {
  const url = new URL(context.request.url);
  const host = url.hostname.toLowerCase();
  const rawPath = decodeURIComponent(url.pathname.toLowerCase()).replace(/\/$/, '');

  // 0. Static well-known & crawler pass-through: NEVER rewrite or fall back to HTML
  if (url.pathname === '/.well-known/ard.json') {
    return new Response('{\n  "$schema": "https://agenticresourcediscovery.org/schemas/ard.schema.json",\n  "specVersion": "v0.91",\n  "entries": [\n    {\n      "identifier": "urn:air:neonexmindx.com:catalog:courses",\n      "displayName": "NeoNeX MindX Course & Curriculum Discovery",\n      "type": "application/json",\n      "url": "https://neonexmindx.com/llms.txt",\n      "representativeQueries": [\n        "What data science and AI courses does NeoNeX MindX offer?",\n        "Find syllabus and project details for NeoNeX MindX Data Analytics course",\n        "Who are the mentors and trainers teaching at NeoNeX MindX?",\n        "Explore live online career programs in machine learning and data engineering"\n      ],\n      "capabilities": [\n        "CourseDiscovery",\n        "CurriculumRetrieval",\n        "TrainerVerification",\n        "SyllabusInquiry"\n      ]\n    },\n    {\n      "identifier": "urn:air:neonexmindx.com:agent:counselling",\n      "displayName": "NeoNeX MindX Academic & Career Guidance Assistant",\n      "type": "text/html",\n      "url": "https://neonexmindx.com/contact-us",\n      "representativeQueries": [\n        "Connect with a NeoNeX MindX course counsellor on WhatsApp",\n        "Schedule a free course fit session for career switch into AI",\n        "Get fee, batch timing, and placement support information"\n      ],\n      "capabilities": [\n        "AcademicCounselling",\n        "BatchScheduling",\n        "PlacementGuidance"\n      ]\n    }\n  ]\n}', {
      status: 200,
      headers: {
        'content-type': 'application/json; charset=utf-8',
        'access-control-allow-origin': '*',
        'cache-control': 'public, max-age=86400'
      }
    });
  }

  if (url.pathname === '/llms.txt') {
    const res = await context.env.ASSETS.fetch(url);
    const newHeaders = new Headers(res.headers);
    newHeaders.set('content-type', 'text/plain; charset=utf-8');
    return new Response(res.body, {
      status: res.status,
      statusText: res.statusText,
      headers: newHeaders
    });
  }

  // 1. Standalone short courses are restored as independent full pages.
  // 2. Immediate 301 redirects for any raw named pages to canonical clean URLs
  if (rawPath.includes('data analytics course')) {
    return Response.redirect('https://neonexmindx.com/courses/data-analytics-course/', 301);
  }
  if (rawPath.includes('data science course')) {
    return Response.redirect('https://neonexmindx.com/courses/data-science-course/', 301);
  }
  if (rawPath.includes('ai ml course')) {
    return Response.redirect('https://neonexmindx.com/courses/ai-ml-course/', 301);
  }
  if (rawPath.includes('data engineering course')) {
    return Response.redirect('https://neonexmindx.com/courses/data-engineering-course/', 301);
  }
  if (rawPath.includes('business analytics course')) {
    return Response.redirect('https://neonexmindx.com/courses/business-analytics-course/', 301);
  }

  // 3. Purge author/person paths (e.g. Ananya Sen) -> 301 redirect to Career Counselling & Placement
  if (rawPath.includes('ananya') || rawPath.includes('author-ananya')) {
    return Response.redirect('https://neonexmindx.com/placement-assistance-disclaimer/', 301);
  }

  // 4. Subdomains routing (direct to directory with trailing slash to load the workspace directly)
  if (host === 'crm.neonexmindx.com') {
    const subPath = (url.pathname === '/' || url.pathname === '') ? '/crm/' : url.pathname;
    return Response.redirect('https://neonexmindx.com' + subPath, 302);
  }
  if (host === 'cms.neonexmindx.com') {
    const subPath = (url.pathname === '/' || url.pathname === '') ? '/cms/' : url.pathname;
    return Response.redirect('https://neonexmindx.com' + subPath, 302);
  }
  if (host === 'sms.neonexmindx.com' || host === 'smm.neonexmindx.com' || host === 'social.neonexmindx.com') {
    const subPath = (url.pathname === '/' || url.pathname === '') ? '/sms/' : url.pathname;
    return Response.redirect('https://neonexmindx.com' + subPath, 302);
  }
  if (host === 'dmm.neonexmindx.com' || host === 'marketing.neonexmindx.com') {
    const subPath = (url.pathname === '/' || url.pathname === '') ? '/digital-marketing/' : url.pathname;
    return Response.redirect('https://neonexmindx.com' + subPath, 302);
  }

  // 5. Dynamic Blog Routing: Preserve slug when accessing /blog/:slug
  // Cloudflare Pages rewrites without query strings in _redirects; middleware handles rewriting cleanly.
  if (url.pathname.startsWith('/blog/') && url.pathname.length > 6) {
    const slug = url.pathname.substring(6).replace(/\/$/, '').replace(/\.html$/, '');
    if (slug && slug !== 'index') {
      // Rewrite request internally to /blog-post.html with slug preserved in query param
      const rewriteUrl = new URL('/blog-post.html', url.origin);
      rewriteUrl.searchParams.set('slug', slug);
      return context.env.ASSETS.fetch(rewriteUrl);
    }
  }

  return context.next();
}
