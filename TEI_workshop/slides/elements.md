[<<<Previous  ](preliminary.md) | [Next>>>](practice.md)

# Elements for Primary Source Encoding 

We are now going to look at some useful elements from the Primary Source Encoding module of the guidelines. These elements represent only a subset of possible elements of this module, which itself is only a subset of the TEI guidelines (the guidelines having over 500 elements total!). The elements below are selected because they are (1) commonly used in this module and (2) directly relevant to the kind of encoding we will be doing today. They are the following: 
    
 **&lt;sourceDoc>**

In primary source encoding, this element is equivalent to the "body" tag in HTML. It encloses the entire second half of the document, and begins after the end tag of the **&lt;teiHeader>**. The document, therefore, should be structured like this:

        <?xml>
        <TEI>
            <teiHeader>
                <...>       ### header
            </teiHeader>
            <sourceDoc>
                <...>       ### body
            </sourceDoc>
        </TEI>
    
 **&lt;surface>**

This is another element that encloses the main body of the document, nested just under the **&lt;sourceDoc>** element. The document, therefore, should look like this:
        
    <?xml>
    <TEI>
        <teiHeader>
            <...>          ### header
        </teiHeader>
        <sourceDoc>
            <surface>
                <...>       ### the rest of your encoding will go in this section
            </surface>
        </sourceDoc>
     </TEI>

Now we have the basic structure of a primary source document in place. We can now turn to the individual lines of the document, and encode it line by line. 
    
 **&lt;line>**

This indicates that a new line has begun in the manuscript. For a diplomatic transcription, you need to enclose each line with the **&lt;line>&lt;/line>** tags, otherwise the line will continuously run across the page. 
    
**&lt;add>** and  **&lt;del>**

Words or phrases that have been added or deleted in the source text may be recorded using **&lt;add>** and **&lt;del>**. Information about the actual rendition of the additions and deletions can be provided in the **@rend** attribute, such as a strikethrough. Additionally, the place of the addition may also be recorded using the **@place** attribute, such as **“above”** or **“below”**, which would display the text either above or below the current line. 

Important to note: The **&lt;del>** element cannot use the **@place** attribute. If you need to use the **@place** attribute, encode with the **&lt;add>** element, and combine with **@rend** set to the value **"strikethrough"**.

Example:

    <line>
        <add>Some added text goes here.</add>
        <add place="above">this text will appear above the current line.</add>
        <del rend="strikethrough">deleted text, with a strikethrough, goes here.</del>
    </line>

    <line>
        <add place="above" rend="strikethrough>this text will appear above the current line, with a strikethrough.</add>
    </line>

 **&lt;mod>**

Additions and deletions with a causal relationship may be grouped by the  **&lt;mod>** element. This is only necessary if more than one action (adding or deleting) affects the same piece of text, such as a deletion that was then replaced with an addition. 

Example: 

    <mod>
        <del>text that was deleted text</del>
        <add>text that was added to replace the deleted text</add>
    </mod>

 **&lt;gap>**

In areas where the source text cannot be read with confidence,  **&lt;gap>** should be used with the **@reason** attribute indicating that the difficulty of transcription is due to illegibility. In those cases where you cannot read the text, you may encode with the following: 

    <gap reason="illegible"></gap>

## Putting it all together

Copy and paste the following into your text editor:
        
    <?xml version="1.0" encoding="UTF-8"?>
    <?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
    <?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml"
        schematypens="http://purl.oclc.org/dsdl/schematron"?>
    <TEI xmlns="http://www.tei-c.org/ns/1.0">
        <teiHeader>
            <fileDesc>
                <titleStmt>
                    <title>The Picture of Dorian Gray: Original Manuscript</title>
                </titleStmt>
                <publicationStmt>
                    <p>Unpublished manuscript</p>
                </publicationStmt>
                <sourceDesc>
                    <p>Wilde, Oscar. "The Picture of Dorian Gray: Original Manuscript." MS. 1889. Morgan Library and Museum. New York, NY.</p>
                </sourceDesc>
            </fileDesc>
        </teiHeader>
        <sourceDoc>
            <surface>
            </surface>
        </sourceDoc>
    </TEI>

[<<<Previous  ](preliminary.md) | [Next>>>](practice.md)