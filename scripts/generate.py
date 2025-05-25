colorscheme = {
  "bg_dim": "#151515",
  "bg0": "#181818",
  "bg1": "#282828",
  "bg2": "#282828",
  "bg3": "#32302f",
  "bg4": "#3c3836",
  "bg5": "#504945",
  "bg_statusline1": "#282828",
  "bg_statusline2": "#32302f",
  "bg_statusline3": "#504945",
  "bg_diff_green": "#32361e",
  "bg_visual_blue": "#333e34",
  "bg_diff_red": "#3c1f1e",
  "bg_visual_red": "#442e2d",
  "bg_diff_blue": "#0d3138",
  "bg_visual_blue": "#2e3b3b",
  "bg_visual_yellow": "#473c29",
  "bg_current_word": "#32302f",
  "fg0": "#ebdbb2",
  "fg1": "#ddc7a1",
  "red": "#fb4934",
  "orange": "#fe8019",
  "yellow": "#fabd2f",
  "green": "#b8bb26",
  "aqua": "#8ec07c",
  "blue": "#83a598",
  "purple": "#d3869b",
  "bg_red": "#fb4934",
  "bg_yellow": "#fabd2f",
  "bg_green": "#b8bb26",
  "grey0": "#7c6f64",
  "grey1": "#928374",
  "grey2": "#a89984",
}

def save_theme(name: str, content: str):
    with open(f"./themes/{name.lower().replace(' ', '_')}.json", "w") as f:
        f.write(content)

def generate_theme(name: str, colors: dict) -> str:
    return f'''
{{
    "name": "Gruvbox Material Mix",
    "type": "dark",
    "semanticHighlighting": true,
    "semanticTokenColors": {{
        "enumMember": {{
            "foreground": "{colors['orange']}"
        }},
        "variable.constant": {{
            "foreground": "{colors['purple']}"
        }},
        "variable.defaultLibrary": {{
            "foreground": "{colors['orange']}"
        }}
    }},
    "tokenColors": [
        {{
            "name": "unison punctuation",
            "scope": "punctuation.definition.delayed.unison,punctuation.definition.list.begin.unison,punctuation.definition.list.end.unison,punctuation.definition.ability.begin.unison,punctuation.definition.ability.end.unison,punctuation.operator.assignment.as.unison,punctuation.separator.pipe.unison,punctuation.separator.delimiter.unison,punctuation.definition.hash.unison",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "support.variable.magic.python",
            "scope": "support.variable.magic.python",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "punctuation.separator.parameters.python",
            "scope": "punctuation.separator.period.python,punctuation.separator.element.python,punctuation.parenthesis.begin.python,punctuation.parenthesis.end.python",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "storage.modifier.lifetime.rust",
            "scope": "storage.modifier.lifetime.rust",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "variable.language.rust",
            "scope": "variable.language.rust",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "regexp constant character-class",
            "scope": "constant.other.character-class.regexp",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "Text",
            "scope": "variable.parameter.function",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "Comment Markup Link",
            "scope": "comment markup.link",
            "settings": {{
                "foreground": "#7c6f64"
            }}
        }},
        {{
            "name": "deleted.diff",
            "scope": "markup.deleted.diff",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "c++ function",
            "scope": "meta.function.c,meta.function.cpp",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "c/c++ block, parens, bracket",
            "scope": [
                "punctuation.section.block.begin.bracket",
                "punctuation.section.block.end.bracket",
                "punctuation.section.arguments.begin.bracket",
                "punctuation.section.arguments.end.bracket",
                "punctuation.section.parens.begin.bracket",
                "punctuation.section.parens.end.bracket",
                "punctuation.section.block.begin.bracket",
                "punctuation.section.block.end.bracket",
                "punctuation.section.parameters.begin.bracket",
                "punctuation.section.parameters.end.bracket",
                "punctuation.separator",
                "punctuation.separator.delimiter.comma",
                "punctuation.definition.capture.begin.lambda",
                "punctuation.definition.capture.end.lambda",
                "punctuation.definition.begin.bracket.square",
                "punctuation.definition.end.bracket.square",
                "punctuation.section.angle-brackets.begin.template",
                "punctuation.section.angle-brackets.end.template",
                "punctuation.terminator.statement"
            ],
            "settings": {{
                "foreground": "{colors['grey0']}"
            }}
        }},
        {{
            "name": "math js/ts",
            "scope": [
                "support.constant.math",
                "support.module.node",
                "support.type.vendored.property-name.css",
                "support.type.object.module",
                "support.type.object.dom",
                "support.type.posix-reserved.c",
                "support.type.posix-reserved.cpp",
                "support.type.python",
                "support.type.swift",
                "support.type.vb.asp",
                "support.type.primitive",
                "support.type.primitive.ts",
                "support.type.builtin.ts",
                "support.type.primitive.tsx",
                "support.type.builtin.tsx",
                "support.type.prelude.elm",
                "support.other.namespace.use.php",
                "support.other.namespace.use-as.php",
                "support.other.namespace.php",
                "support.token.decorator.python",
                "support.class",
                "support.function",
                "support.variable.semantic.hlsl",
                "variable.other.class.js",
                "variable.other.class.ts",
                "variable.other.constant",
                "variable.language",
                "variable.parameter.function.language.special.self.python",
                "storage.type.annotation.java",
                "storage.type.object.array.java",
                "storage.type.java",
                "storage.type.generic.java",
                "storage.type.cs",
                "storage.type.php",
                "storage.modifier.import.java",
                "storage.modifier.import.groovy",
                "storage.modifier.reference",
                "keyword.other.type.php",
                "keyword.other.array.phpdoc.php",
                "keyword.control.xi",
                "keyword.operator",
                "keyword.operator.expression.instanceof",
                "keyword.operator.new",
                "keyword.operator.ternary",
                "keyword.operator.optional",
                "keyword.operator.expression.keyof",
                "keyword.operator.sigil.rust",
                "keyword.operator.delete",
                "keyword.operator.arithmetic",
                "keyword.operator.comparison,keyword.operator.decrement",
                "keyword.operator.increment,keyword.operator.relational",
                "keyword.operator.comparison.c",
                "keyword.operator.comparison.cpp",
                "keyword.operator.c",
                "keyword.operator.cpp",
                "keyword.operator.increment.c",
                "keyword.operator.increment.cpp",
                "keyword.operator.decrement.c",
                "keyword.operator.decrement.cpp",
                "keyword.operator.bitwise",
                "keyword.operator.bitwise.shift.c",
                "keyword.operator.bitwise.shift.cpp",
                "keyword.operator.assignment.compound.js",
                "keyword.operator.assignment.compound.ts",
                "keyword.operator.assignment",
                "keyword.operator.assignment.go",
                "keyword.operator.assignment.c",
                "keyword.operator.assignment.cpp",
                "keyword.operator.comparison.php",
                "keyword.operator.logical",
                "keyword.operator.logical.php",
                "keyword.operator.bitwise.php",
                "keyword.operator.arithmetic.php",
                "entity.name.namespace",
                "entity.name.type.namespace",
                "entity.name.type.class",
                "entity.name.class.identifier.namespace.type",
                "entity.name.class",
                "entity.name.type",
                "entity.name.type.module",
                "entity.name.tag.html",
                "entity.name.label.cs",
                "entity.name.scope-resolution.function.call",
                "entity.name.scope-resolution.function.definition",
                "entity.name.function.xi",
                "entity.name.class.xi",
                "entity.name.package.go",
                "entity.name.lifetime.rust",
                "entity.other.attribute-name.pseudo-element",
                "entity.other.attribute-name.pseudo-class",
                "entity.other.alias.php",
                "entity.other.inherited-class",
                "entity.global.clojure",
                "constant.other.symbol",
                "constant.other.color.rgb-value.xi",
                "constant.language.symbol.elixir",
                "constant.keyword.clojure",
                "constant.character.escape",
                "constant.language.symbol.ruby",
                "punctuation.definition.tag.begin.html",
                "punctuation.definition.tag.end.html",
                "punctuation.definition.bold",
                "punctuation.separator.pointer-access",
                "source.makefile",
                "source.json meta.structure.dictionary.json > constant.language.json",
                "source.json meta.structure.array.json > constant.language.json",
                "meta.method.groovy",
                "meta.function.decorator.identifier.python",
                "meta.interface.php",
                "meta.other.type.phpdoc.php",
                "import.storage.java",
                "token.storage.type.java",
                "rgb-value",
                "markup.changed.diff",
                "string.regexp"
            ],
            "settings": {{
                "foreground": "{colors['orange']}"
            }}
        }},
        {{
            "name": "java source",
            "scope": "source.java",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "java modifier.import",
            "scope": "punctuation.section.block.begin.java,punctuation.section.block.end.java,punctuation.definition.method-parameters.begin.java,punctuation.definition.method-parameters.end.java,meta.method.identifier.java,punctuation.section.method.begin.java,punctuation.section.method.end.java,punctuation.terminator.java,punctuation.section.class.begin.java,punctuation.section.class.end.java,punctuation.section.inner-class.begin.java,punctuation.section.inner-class.end.java,meta.method-call.java,punctuation.section.class.begin.bracket.curly.java,punctuation.section.class.end.bracket.curly.java,punctuation.section.method.begin.bracket.curly.java,punctuation.section.method.end.bracket.curly.java,punctuation.separator.period.java,punctuation.bracket.angle.java,punctuation.definition.annotation.java,meta.method.body.java",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "java variable.name",
            "scope": "meta.definition.variable.name.java",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "css comma",
            "scope": "punctuation.separator.list.comma.css",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "js variable readwrite",
            "scope": "variable.other.readwrite,meta.object-literal.key,support.variable.property,support.variable.object.process,support.variable.object.node",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "keyword.operator.misc.rust",
            "scope": "keyword.operator.misc.rust",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "js dom variable",
            "scope": "support.variable.dom,support.variable.property.dom",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "Punctuation",
            "scope": "punctuation.separator.delimiter",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "js/ts console",
            "scope": "support.type.object.console",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "python block",
            "scope": "punctuation.definition.arguments.begin.python,punctuation.definition.arguments.end.python,punctuation.separator.arguments.python,punctuation.definition.list.begin.python,punctuation.definition.list.end.python",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "Operators",
            "scope": "keyword.operator",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "Variables",
            "scope": "variable",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "Variables",
            "scope": "variable.c",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "Java Variables",
            "scope": "token.variable.parameter.java",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "Packages",
            "scope": "token.package",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "name": "Class name php",
            "scope": "variable.other.class.php",
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "scope": [
                "support.type.type.flowtype",
                "support.function.std.rust",
                "support.other.php",
                "keyword.operator.expression.import",
                "keyword.other.special-method",
                "keyword.operator.sizeof.c",
                "keyword.operator.sizeof.cpp",
                "punctuation.definition.from-file.diff",
                "punctuation.definition.to-file.diff",
                "punctuation.definition.tag.xi",
                "markup.heading punctuation.definition.heading",
                "markup.quote.markdown",
                "entity.name.section",
                "entity.other.attribute-name.id",
                "entity.name.goto-label.php",
                "string.other.link.title.markdown",
                "string.other.link.description.markdown",
                "meta.function.decorator.python",
                "meta.diff.header.from-file",
                "meta.diff.header.to-file",
                "meta.method.java",
                "meta.function-call.generic.python",
                "accent.xi",
                "constant.character.xi"
            ],
            "settings": {{
                "foreground": "{colors['aqua']}"
            }}
        }},
        {{
            "scope": [
                "storage.type.built-in",
                "entity.name.scope-resolution",
                "entity.name.type",
                "meta.body.class",
                "token.storage"

            ],
            "settings": {{
                "foreground": "{colors['yellow']}"
            }}
        }},
        {{
            "scope": [
                "keyword",
                "keyword.control",
                "keyword.operator.expression.delete",
                "keyword.operator.expression.in",
                "keyword.operator.expression.of",
                "keyword.operator.expression.instanceof",
                "keyword.operator.new",
                "keyword.operator.expression.typeof",
                "keyword.operator.expression.void",
                "keyword.operator.arithmetic.go",
                "keyword.operator.address.go",
                "keyword.operator.module",
                "keyword.operator.regexp.php",
                "keyword.operator.error-control.php",
                "keyword.operator.type.php",
                "keyword.operator.heredoc.php",
                "keyword.operator.nowdoc.php",
                "keyword.operator.assignment.compound",
                "keyword.operator.logical.python",
                "keyword.operator.instanceof.java",
                "support.constant.edge",
                "support.type.texture.hlsl",
                "support.type.sampler.hlsl",
                "support.type.object.hlsl",
                "support.type.object.rw.hlsl",
                "support.type.fx.hlsl",
                "punctuation.definition.template-expression.begin",
                "punctuation.definition.template-expression.end",
                "punctuation.section.embedded",
                "punctuation.section.embedded.begin,punctuation.section.embedded.end",
                "punctuation.definition.italic,todo.emphasis",
                "punctuation.quasi.element",
                "punctuation.separator.c",
                "punctuation.separator.cpp",
                "token.debug-token",
                "token.package.keyword",
                "storage.type.class.cpp",
                "storage.type.enum.cpp",
                "storage.type.modifier.access.control",
                "storage.modifier.inline",
                "storage.modifier.specifier.static",
                "text.html.laravel-blade source.php.embedded.line.html entity.name.tag.laravel-blade",
                "texthtml.laravel-blade source.php.embedded.line.html support.constant.laravel-blade",
                "markup.italic",
                "markup.underline.link.markdown",
                "markup.underline.link.image.markdown",
                "emphasis md",
                "meta.selector",
                "constant.regexp.xi",
                "variable.other.generic-type.haskell"
            ],
            "settings": {{
                "foreground": "{colors['red']}"
            }}
        }},
        {{
            "scope": [
                "punctuation.separator.key-value",
                "punctuation.definition.list.begin.markdown",
                "punctuation.definition.heading.markdown",
                "punctuation.definition.list.markdown",
                "punctuation.definition.string.begin.markdown",
                "punctuation.definition.string.end.markdown",
                "punctuation.definition.metadata.markdown",
                "punctuation.definition.metadata.markdown",
                "punctuation.section.embedded, variable.interpolation",
                "punctuation.section.array.begin.php",
                "punctuation.section.array.end.php",
                "punctuation.definition.parameters.begin.bracket.round.php",
                "punctuation.definition.parameters.end.bracket.round.php",
                "punctuation.separator.delimiter.php",
                "punctuation.section.scope.begin.php",
                "punctuation.section.scope.end.php",
                "punctuation.terminator.expression.php",
                "punctuation.definition.arguments.begin.bracket.round.php",
                "punctuation.definition.arguments.end.bracket.round.php",
                "punctuation.definition.storage-type.begin.bracket.round.php",
                "punctuation.definition.storage-type.end.bracket.round.php",
                "punctuation.definition.array.begin.bracket.round.php",
                "punctuation.definition.array.end.bracket.round.php",
                "punctuation.definition.begin.bracket.round.php",
                "punctuation.definition.end.bracket.round.php",
                "punctuation.definition.begin.bracket.curly.php",
                "punctuation.definition.end.bracket.curly.php",
                "punctuation.definition.section.switch-block.end.bracket.curly.php",
                "punctuation.definition.section.switch-block.start.bracket.curly.php",
                "punctuation.definition.section.switch-block.begin.bracket.curly.php",
                "punctuation.definition.section.switch-block.end.bracket.curly.php",
                "punctuation.definition.block.sequence.item.yaml",
                "support.type.property-name",
                "support.constant.property-value",
                "support.type.property-name.json",
                "support.type.property-name.json punctuation",
                "function.parameter",
                "function.brace",
                "function.parameter.ruby",
                "function.parameter.cs",
                "entity.name.tag",
                "entity.name.section.markdown",
                "entity.name.variable.local.cs",
                "markup.heading",
                "markup.heading.setext",
                "markup.heading.setext.1.markdown",
                "markup.heading.setext.2.markdown",
                "meta.tag",
                "meta.template.expression",
                "meta.property.object",
                "meta.definition.variable.name.groovy",
                "meta.scope.prerequisites.makefile",
                "meta.symbol.clojure",
                "meta.arguments.coffee",
                "meta.brace.square",
                "source.json meta.structure.dictionary.json > string.quoted.json",
                "source.json meta.structure.dictionary.json > string.quoted.json > punctuation.string",
                "invalid.illegal.bad-ampersand.html",
                "beginning.punctuation.definition.list.markdown",
                "block.scope.end",
                "block.scope.begin",
                "entity.name.label.cs",
                "text.variable",
                "text.bracketed",
                "variable.parameter.function.coffee",
                "variable.parameter.function.js",
                "constant.character.entity",
                "constant.character.character-class.regexp.xi",
                "selector.sass",
                "invalid.xi"
            ],
            "settings": {{
                "foreground": "{colors['fg0']}"
            }}
        }},
        {{
            "scope": [
                "string",
                "keyword.other.template.end",
                "keyword.other.template.begin",
                "keyword.other.substitution.begin",
                "keyword.other.substitution.end",
                "source.json meta.structure.dictionary.json > value.json > string.quoted.json",
                "source.json meta.structurekarray.json > value.json > string.quoted.json",
                "source.json meta.structure.dictionary.json > value.json > string.quoted.json > punctuation",
                "source.json meta.structure.array.json > value.json > string.quoted.json > punctuation",
                "markup.inserted.diff",
                "markup.inline.raw.markdown",
                "markup.inline.raw.string.markdown",
                "meta.function-call.php,meta.function-call.object.php,meta.function-call.static.php",
                "meta.definition.class.inherited.classes.groovy",
                "meta.require",
                "entity.name.function",
                "entity.name.function,support.function.console",
                "source.ini",
                "punctuation.definition.string.begin,punctuation.definition.string.end",
                "beginning.punctuation.definition.quote.markdown.xi",
                "variable.function",
                "support.function.any-method"
            ],
            "settings": {{
                "foreground": "{colors['green']}"
            }}
        }},
        {{
            "scope": [
                "constant.numeric",
                "constant",
                "constant.character.format.placeholder.other.python",
                "entity.other.attribute-name",
                "entity.other.attribute-name.class.css",
                "punctuation.definition.bold.markdown",
                "punctuation.definition.constant",
                "support.constant.property.math",
                "support.constant.property-value.scss,support.constant.property-value.css",
                "support.constant.color.w3c-standard-color-name.css,support.constant.color.w3c-standard-color-name.scss",
                "support.constant.color.w3c-standard-color-name.css",
                "support.constant.json",
                "support.variable.property.process",
                "support.constant.font-name",
                "support.constant.elm",
                "support.constant.core.rust",
                "support.constant.ext.php",
                "support.constant.std.php",
                "support.constant.core.php",
                "support.constant.parser-token.php",
                "variable.parameter.function.python",
                "variable.parameter.function.language.python",
                "storage.type.haskell",
                "keyword.operator.quantifier.regexp",
                "keyword.other.unit",
                "inline-color-decoration rgb-value",
                "token.warn-token",
                "control.elements, keyword.operator.less",
                "wikiword.xi",
                "less rgb-value",
                "markup.bold",
                "todo.bold"
            ],
            "settings": {{
                "foreground": "{colors['purple']}"
            }}
        }},
        {{
            "scope": [
                "variable.other.enummember"
            ],
            "settings": {{
                "foreground": "{colors['blue']}"
            }}
        }},
        {{
            "name": "illegal",
            "scope": "invalid.illegal",
            "settings": {{
                "foreground": "#ffffff"
            }}
        }},
        {{
            "name": "Broken",
            "scope": "invalid.broken",
            "settings": {{
                "foreground": "#ffffff"
            }}
        }},
        {{
            "name": "Deprecated",
            "scope": "invalid.deprecated",
            "settings": {{
                "foreground": "#ffffff"
            }}
        }},
        {{
            "name": "Unimplemented",
            "scope": "invalid.unimplemented",
            "settings": {{
                "foreground": "#ffffff"
            }}
        }},
        {{
            "name": "php illegal.non-null-typehinted",
            "scope": "invalid.illegal.non-null-typehinted.php",
            "settings": {{
                "foreground": "#f44747"
            }}
        }},
        {{
            "scope": "token.error-token",
            "settings": {{
                "foreground": "#f44747"
            }}
        }},
        {{
            "name": "comments",
            "scope": [
                "beginning.punctuation.definition.list.markdown.xi"
            ],
            "settings": {{
                "foreground": "#7c6f64"
            }}
        }},
        {{
            "name": "Comments",
            "scope": "comment, punctuation.definition.comment",
            "settings": {{
                "fontStyle": "italic",
                "foreground": "#7c6f64"
            }}
        }},
        {{
            "name": "js/ts italic",
            "scope": "entity.other.attribute-name.js,entity.other.attribute-name.ts,entity.other.attribute-name.jsx,entity.other.attribute-name.tsx,variable.parameter,variable.language.super",
            "settings": {{
                "fontStyle": "italic"
            }}
        }},
        {{
            "name": "comment",
            "scope": "comment.line.double-slash,comment.block.documentation",
            "settings": {{
                "fontStyle": "italic"
            }}
        }},
        {{
            "name": "Python Keyword Control",
            "scope": "keyword.control.import.python,keyword.control.flow.python",
            "settings": {{
                "fontStyle": "italic"
            }}
        }},
        {{
            "name": "markup.italic.markdown",
            "scope": "markup.italic.markdown",
            "settings": {{
                "fontStyle": "italic"
            }}
        }}
    ],
    "colors": {{
        "foreground": "{colors['fg0']}",
        "focusBorder": "{colors['green']}",
        "selection.background": "{colors['blue']}",
        "scrollbar.shadow": "#00000000",
        "activityBar.foreground": "{colors['fg0']}",
        "activityBar.background": "{colors['bg0']}",
        "activityBar.inactiveForeground": "{colors['bg3']}",
        "activityBarBadge.foreground": "{colors['bg0']}",
        "activityBarBadge.background": "{colors['green']}",
        "activityBar.border": "{colors['bg3']}",
        "sideBar.background": "{colors['bg_dim']}",
        "sideBar.foreground": "{colors['fg0']}",
        "sideBarSectionHeader.background": "{colors['bg0']}",
        "sideBarSectionHeader.foreground": "{colors['green']}",
        "sideBarSectionHeader.border": "{colors['fg0']}00",
        "sideBarTitle.foreground": "{colors['green']}",
        "sideBar.border": "{colors['bg3']}",
        "list.inactiveSelectionBackground": "{colors['bg0']}",
        "list.inactiveSelectionForeground": "{colors['green']}",
        "list.hoverBackground": "{colors['bg0']}",
        "list.hoverForeground": "{colors['green']}",
        "list.activeSelectionBackground": "{colors['bg0']}",
        "list.activeSelectionForeground": "#b0b856",
        "tree.indentGuidesStroke": "{colors['fg0']}33",
        "list.dropBackground": "{colors['bg_dim']}",
        "list.highlightForeground": "{colors['orange']}",
        "list.focusBackground": "{colors['bg0']}",
        "list.focusForeground": "{colors['fg0']}",
        "listFilterWidget.background": "{colors['blue']}",
        "listFilterWidget.outline": "#00000000",
        "listFilterWidget.noMatchesOutline": "{colors['red']}00",
        "statusBar.foreground": "{colors['fg0']}",
        "statusBar.background": "{colors['bg_dim']}",
        "statusBarItem.hoverBackground": "{colors['bg0']}",
        "statusBar.border": "{colors['bg3']}",
        "statusBar.debuggingBackground": "{colors['bg_dim']}",
        "statusBar.debuggingForeground": "{colors['fg0']}",
        "statusBar.noFolderBackground": "{colors['bg_dim']}",
        "statusBar.noFolderForeground": "{colors['fg0']}",
        "statusBarItem.remoteBackground": "{colors['green']}",
        "statusBarItem.remoteForeground": "{colors['bg_dim']}",
        "titleBar.activeBackground": "{colors['bg_dim']}",
        "titleBar.activeForeground": "{colors['fg0']}",
        "titleBar.inactiveBackground": "{colors['bg_dim']}",
        "titleBar.inactiveForeground": "{colors['fg0']}99",
        "titleBar.border": "{colors['bg3']}",
        "menubar.selectionForeground": "{colors['green']}",
        "menubar.selectionBackground": "{colors['bg0']}",
        "menubar.selectionBorder": "#ff000000",
        "menu.foreground": "{colors['fg0']}",
        "menu.background": "{colors['bg_dim']}",
        "menu.selectionForeground": "{colors['green']}",
        "menu.selectionBackground": "{colors['bg0']}",
        "menu.selectionBorder": "#00000000",
        "menu.separatorBackground": "{colors['fg0']}33",
        "menu.border": "{colors['bg_dim']}",
        "button.background": "{colors['green']}",
        "button.foreground": "{colors['bg2']}",
        "button.hoverBackground": "{colors['green']}99",
        "button.secondaryForeground": "{colors['fg0']}",
        "button.secondaryBackground": "{colors['bg0']}",
        "button.secondaryHoverBackground": "{colors['bg0']}99",
        "input.background": "{colors['bg0']}",
        "input.border": "#00000000",
        "input.foreground": "{colors['fg0']}",
        "inputOption.activeBackground": "{colors['green']}66",
        "inputOption.activeBorder": "#007acc00",
        "inputOption.activeForeground": "{colors['fg0']}",
        "input.placeholderForeground": "{colors['fg0']}33",
        "textLink.foreground": "{colors['blue']}",
        "editor.background": "{colors['bg0']}",
        "editor.foreground": "{colors['fg0']}",
        "editorLineNumber.foreground": "#928374",
        "editorCursor.foreground": "{colors['fg0']}66",
        "editorCursor.background": "{colors['fg0']}",
        "editor.selectionBackground": "{colors['bg4']}",
        "editor.inactiveSelectionBackground": "{colors['bg2']}90",
        "editorWhitespace.foreground": "#e2cca929",
        "editor.selectionHighlightBackground": "#add6ff26",
        "editor.selectionHighlightBorder": "#495F77",
        "editor.findMatchBackground": "#515c6a",
        "editor.findMatchBorder": "#74879f",
        "editor.findMatchHighlightBackground": "#ea5c0055",
        "editor.findMatchHighlightBorder": "#ffffff00",
        "editor.findRangeHighlightBackground": "#3a3d4166",
        "editor.findRangeHighlightBorder": "#ffffff00",
        "editor.rangeHighlightBackground": "#ffffff0b",
        "editor.rangeHighlightBorder": "#ffffff00",
        "editor.hoverHighlightBackground": "#264f7840",
        "editor.wordHighlightStrongBackground": "#004972b8",
        "editor.wordHighlightBackground": "#575757b8",
        "editor.lineHighlightBackground": "#ffffff0A",
        "editor.lineHighlightBorder": "{colors['bg2']}",
        "editorLineNumber.activeForeground": "{colors['fg0']}",
        "editorLink.activeForeground": "{colors['blue']}",
        "editorIndentGuide.background1": "{colors['bg2']}",
        "editorIndentGuide.activeBackground1": "{colors['green']}",
        "editorRuler.foreground": "{colors['bg2']}",
        "editorBracketMatch.background": "#0064001a",
        "editorBracketMatch.border": "#888888",
        "editor.foldBackground": "#264f784d",
        "editorOverviewRuler.background": "#25252500",
        "editorOverviewRuler.border": "#7f7f7f4d",
        "editorError.foreground": "#f48771",
        "editorError.background": "#B73A3400",
        "editorError.border": "#ffffff00",
        "editorWarning.foreground": "#cca700",
        "editorWarning.background": "#A9904000",
        "editorWarning.border": "#ffffff00",
        "editorInfo.foreground": "#75beff",
        "editorInfo.background": "#4490BF00",
        "editorInfo.border": "#4490BF00",
        "editorGutter.background": "{colors['bg0']}",
        "editorGutter.modifiedBackground": "{colors['blue']}",
        "editorGutter.addedBackground": "{colors['green']}",
        "editorGutter.deletedBackground": "{colors['red']}",
        "editorGutter.foldingControlForeground": "#c5c5c5",
        "editorCodeLens.foreground": "#999999",
        "editorGroup.border": "{colors['bg3']}",
        "diffEditor.insertedTextBackground": "#9bb95533",
        "diffEditor.removedTextBackground": "#ff000033",
        "diffEditor.border": "{colors['bg3']}",

        "panel.background": "{colors['bg_dim']}",
        "panel.border": "{colors['fg0']}33",
        "panelTitle.activeBorder": "{colors['fg0']}",
        "panelTitle.activeForeground": "{colors['fg0']}",
        "panelTitle.inactiveForeground": "{colors['fg0']}99",
        "badge.background": "{colors['orange']}",
        "badge.foreground": "{colors['bg0']}",
        "terminal.foreground": "{colors['fg0']}",
        "terminal.selectionBackground": "{colors['bg2']}40",
        "terminalCursor.background": "{colors['green']}",
        "terminalCursor.foreground": "{colors['fg0']}ee",
        "terminal.border": "{colors['bg0']}",
        "terminal.ansiBlack": "{colors['bg2']}",
        "terminal.ansiBlue": "{colors['blue']}",
        "terminal.ansiBrightBlack": "{colors['bg3']}",
        "terminal.ansiBrightBlue": "{colors['blue']}",
        "terminal.ansiBrightCyan": "{colors['aqua']}",
        "terminal.ansiBrightGreen": "{colors['green']}",
        "terminal.ansiBrightMagenta": "{colors['purple']}",
        "terminal.ansiBrightRed": "{colors['red']}",
        "terminal.ansiBrightWhite": "{colors['fg0']}",
        "terminal.ansiBrightYellow": "{colors['yellow']}",
        "terminal.ansiCyan": "{colors['aqua']}",
        "terminal.ansiGreen": "{colors['green']}",
        "terminal.ansiMagenta": "{colors['purple']}",
        "terminal.ansiRed": "{colors['red']}",
        "terminal.ansiWhite": "{colors['fg0']}",
        "terminal.ansiYellow": "{colors['yellow']}",

        "breadcrumb.background": "{colors['bg0']}",
        "breadcrumb.foreground": "{colors['fg0']}cc",
        "breadcrumb.focusForeground": "{colors['fg0']}cc",
        "editorGroupHeader.tabsBackground": "{colors['bg_dim']}",
        "editorGroupHeader.tabsBorder": "{colors['bg3']}",
        "editorGroupHeader.border": "{colors['bg3']}",
        "tab.activeForeground": "{colors['fg0']}",
        "tab.border": "{colors['bg3']}",
        "tab.activeBackground": "{colors['bg0']}",
        "tab.activeBorder": "{colors['bg0']}",
        "tab.activeBorderTop": "{colors['green']}",
        "tab.inactiveBackground": "{colors['bg_dim']}",
        "tab.inactiveForeground": "{colors['fg0']}50",

        "scrollbarSlider.background": "{colors['bg2']}",
        "scrollbarSlider.hoverBackground": "{colors['bg2']}90",
        "scrollbarSlider.activeBackground": "#ffffff12",
        "progressBar.background": "{colors['green']}",
        "widget.shadow": "#00000070",
        "editorWidget.foreground": "{colors['fg0']}",
        "editorWidget.background": "{colors['bg_dim']}",
        "editorWidget.resizeBorder": "#5f5f5f33",
        "pickerGroup.border": "#00000000",
        "pickerGroup.foreground": "{colors['yellow']}",
        "debugToolBar.background": "{colors['bg0']}",
        "debugToolBar.border": "{colors['fg0']}33",

        "notifications.foreground": "{colors['fg0']}",
        "notifications.background": "{colors['bg0']}",
        "notificationToast.border": "{colors['fg0']}33",
        "notificationsErrorIcon.foreground": "{colors['red']}",
        "notificationsWarningIcon.foreground": "{colors['yellow']}",
        "notificationsInfoIcon.foreground": "{colors['blue']}",
        "notificationCenter.border": "{colors['fg0']}33",
        "notificationCenterHeader.foreground": "{colors['fg0']}",
        "notificationCenterHeader.background": "{colors['bg_dim']}",
        "notifications.border": "{colors['fg0']}33",

        "gitDecoration.addedResourceForeground": "{colors['aqua']}",
        "gitDecoration.conflictingResourceForeground": "{colors['orange']}",
        "gitDecoration.deletedResourceForeground": "{colors['red']}",
        "gitDecoration.ignoredResourceForeground": "{colors['fg0']}33",
        "gitDecoration.modifiedResourceForeground": "{colors['yellow']}",
        "gitDecoration.stageDeletedResourceForeground": "{colors['red']}",
        "gitDecoration.stageModifiedResourceForeground": "#e2cca9",
        "gitDecoration.submoduleResourceForeground": "{colors['blue']}",
        "gitDecoration.untrackedResourceForeground": "#4a7350",
        "editorMarkerNavigation.background": "#2d2d30",
        "editorMarkerNavigationError.background": "#f48771",
        "editorMarkerNavigationWarning.background": "#cca700",
        "editorMarkerNavigationInfo.background": "#75beff",
        "merge.currentHeaderBackground": "#367366",
        "merge.currentContentBackground": "#27403B",
        "merge.incomingHeaderBackground": "{colors['blue']}",
        "merge.incomingContentBackground": "#28384B",
        "merge.commonHeaderBackground": "#383838",
        "merge.commonContentBackground": "{colors['bg2']}",
        "editorSuggestWidget.background": "{colors['bg0']}",
        "editorSuggestWidget.border": "{colors['bg2']}",
        "editorSuggestWidget.foreground": "{colors['fg0']}90",
        "editorSuggestWidget.highlightForeground": "{colors['green']}",
        "editorSuggestWidget.selectedBackground": "{colors['green']}20",
        "editorSuggestWidget.selectedForeground": "{colors['fg0']}90",
        "editorSuggestWidget.selectedIconForeground": "{colors['fg0']}90",
        "editorHoverWidget.foreground": "#cccccc",
        "editorHoverWidget.background": "{colors['bg0']}",
        "editorHoverWidget.border": "{colors['bg2']}",
        "peekView.border": "{colors['blue']}",
        "peekViewEditor.background": "#2e3b3b",
        "peekViewEditorGutter.background": "#2e3b3b",
        "peekViewEditor.matchHighlightBackground": "#ff8f0099",
        "peekViewEditor.matchHighlightBorder": "{colors['yellow']}",
        "peekViewResult.background": "{colors['bg0']}",
        "peekViewResult.fileForeground": "#ffffff",
        "peekViewResult.lineForeground": "#bbbbbb",
        "peekViewResult.matchHighlightBackground": "#ea5c004d",
        "peekViewResult.selectionBackground": "#3399ff33",
        "peekViewResult.selectionForeground": "#ffffff",
        "peekViewTitle.background": "#1e1e1e",
        "peekViewTitleDescription.foreground": "#ccccccb3",
        "peekViewTitleLabel.foreground": "#ffffff",
        "icon.foreground": "{colors['fg0']}",
        "checkbox.background": "{colors['bg_dim']}",
        "checkbox.foreground": "{colors['fg0']}",
        "checkbox.border": "#00000000",
        "dropdown.background": "{colors['bg_dim']}",
        "dropdown.foreground": "{colors['fg0']}",
        "dropdown.border": "#00000000",
        "minimapGutter.addedBackground": "{colors['green']}",
        "minimapGutter.modifiedBackground": "{colors['blue']}",
        "minimapGutter.deletedBackground": "{colors['red']}",
        "minimap.findMatchHighlight": "#515c6a",
        "minimap.selectionHighlight": "{colors['bg2']}90",
        "minimap.errorHighlight": "#f48771",
        "minimap.warningHighlight": "#cca700",
        "minimap.background": "{colors['bg_dim']}",
        "sideBar.dropBackground": "{colors['bg_dim']}",
        "editorGroup.emptyBackground": "{colors['bg_dim']}",
        "panelSection.border": "{colors['fg0']}33",
        "statusBarItem.activeBackground": "#FFFFFF25",
        "settings.headerForeground": "{colors['fg0']}",
        "settings.focusedRowBackground": "#ffffff07",
        "walkThrough.embeddedEditorBackground": "#00000050",
        "breadcrumb.activeSelectionForeground": "{colors['fg0']}cc",
        "editorGutter.commentRangeForeground": "#c5c5c5",
        "debugExceptionWidget.background": "{colors['bg0']}",
        "debugExceptionWidget.border": "{colors['fg0']}33",
        "editorBracketPairGuide.activeBackground1": "{colors['fg0']}cc"
    }}
}}
'''

if __name__ == "__main__":
    theme_name = "Gruvbox Material Mix"
    theme_content = generate_theme(theme_name, colorscheme)
    save_theme(theme_name, theme_content)
    print(f"Theme '{theme_name}' has been generated!")