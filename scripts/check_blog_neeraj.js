const fs = require('fs');

function checkBlog(file) {
    if (!fs.existsSync(file)) return;
    const html = fs.readFileSync(file, 'utf8');
    console.log(`\n=== Blog: ${file} ===`);
    // Find all links to neeraj linkedin
    const neerajLinks = html.match(/https:\/\/www\.linkedin\.com\/in\/neeraj-neonexmindx\/?/g) || [];
    console.log(`  Neeraj LinkedIn mentions: ${neerajLinks.length}`);
    
    // Find author text
    const authorMatches = html.match(/Written by ([^<\n]+)/g) || [];
    console.log(`  Author matches: ${authorMatches.join(', ')}`);
}

const blogs = [
    'deployment_NeoNex/blog.html',
    'deployment_NeoNex/blog-post.html',
    'deployment_NeoNex/blog/data-analytics-portfolio-how-to-build-one-in-2026/index.html',
    'deployment_NeoNex/blog/complete-roadmap-to-become-data-scientist-2026/index.html',
    'deployment_NeoNex/blog/top-high-paying-data-analytics-tools-2026/index.html',
    'deployment_NeoNex/blog/how-neonex-mindx-helps-non-tech-learners-transition/index.html',
    'deployment_NeoNex/blog/modern-data-engineering-pipelines-kafka-spark-cloud/index.html',
    'deployment_NeoNex/blog/machine-learning-vs-deep-learning-differences-guide/index.html',
    'deployment_NeoNex/blog/generative-ai-llm-enterprise-deployment-strategies/index.html',
    'deployment_NeoNex/blog/2026-breakthroughs-in-ai-agents-llms/index.html',
    'deployment_NeoNex/blog/distributed-data-pipelines-with-apache-spark-iceberg/index.html'
];

blogs.forEach(checkBlog);

