CSS_PATH := "src/fasthapix/statics/css"

# run css tasks
[group('css')]
css: gen-css

# generate css
[group('css')]
gen-css:
    uv run tailwindcss -i {{CSS_PATH}}/base.css -o {{CSS_PATH}}/fasthapix.css
    uv run tailwindcss -i {{CSS_PATH}}/base.css -o {{CSS_PATH}}/fasthapix-opt.css --optimize
    uv run tailwindcss -i {{CSS_PATH}}/base.css -o {{CSS_PATH}}/fasthapix-min.css --minify
