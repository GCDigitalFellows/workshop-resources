[<<<Previous  ](modules.md) | [Next>>>](preliminary.md)

# Basic Architecture

In this next section, I'm going to review all of the necessary components to create a TEI document. A lot of this information will be overwhelming for beginners, so it's important to emphasize that you *don't need to know all of it*. These guidelines will stay right here (and much more is easily available through a google search) for you to refer to as you work through your encoding. Even experienced TEI encoders often refer to the guidelines or a web search to refresh certain rules and concepts. 

The most important takeaway from this page---which you *do* need to understand---is the two part structure of the TEI document, that includes a header section and a body section. Let's jump into the header.

## The Head

Like HTML, every TEI document consists of a two parts, a head and a body. We will begin with the head, which describes the source text's metadata, and go through each element in the head one by one. 

Under the DTD declaration, the first line of any TEI document contains the **&lt;TEI>** element itself, which contains an attribute that points to a *namespace*. This namespace is simply used to make sure there are no errors in processing the element names. Accordingly, the TEI element looks like the following:

    <TEI xmlns="http://www.tei-c.org/ns/1.0">

After this **&lt;TEI>** element, the first four elements which make up most of the header are the following, nested from outer to inner element: 

**&lt;teiHeader>** -- Contains the header section, including fileDesc sections \
**&lt;fileDesc>** -- Contains the titleStmt section \
**&lt;titleStmt>** -- Contains the title section \
**&lt;title>** -- Contains the textual description of the title of the source

As you might have guessed, each of these opening tags is followed by an end tag. 

Like the title elements, the next two elements are also nested by the fileDesc. These are the publication and source info.

**&lt;publicationStmt>** -- Describes publication or distribution status of a source text.\
**&lt;sourceDesc>** -- Describes where the source text was derived or generated, typically a bibliographic statement.

Though this might seem like a lot, there are many *more* elements that you could include in the header to describe metadata about the source text. The ones above are only the *minimum* required by the TEI schema. All together, properly nested and populated, the header should look soemthing like this:


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
                <p>Wilde, Oscar. "The Picture of Dorian Gray: Original Manuscript." MS. 1889. Morgan Library & Museum. New York, NY.</p>
            </sourceDesc>
        </fileDesc>
    </teiHeader>

This is a lot of information for now--but don't worry! For our class exercise, you don't need to work with the header at all. Your encoding work will be focusing solely on the body section. So, if the header is TMI for now, you can always come back to it later. 

## The Body

The body section is the second half of a TEI document, and it forms the main section of the document. When a TEI document is transformed, all you will see is the body section. It is important to remember that this section, *along with the header*, is enclosed by the TEI tags.

The header section ends with a TEI header end tag: **&lt;/teiHeader>**. The body section begins with a **&lt;sourceDoc>**. This tag will enclose the entirety of the body. These outer tags for the head and body, nested with TEI tags, therefore, look like this:

    <TEI> # this opens the TEI document
        <teiHeader> # this opens the head
            <...> # header info goes in here
        </teiHeader> # this closes the head
        <sourceDoc> # this opens the body
            <...> # body info goes in here
        </sourceDoc> # this closes the body
    </TEI> # this closes the TEI document

For our purposes, you might think of the **&lt;sourceDoc>** element a "body" tag in HTML. It functions in just the same way. 

The TEI element, being the most outer tag, encloses all the text on the document. It's end tag looks like this: **&lt;/TEI>**

[<<<Previous  ](modules.md) | [Next>>>](preliminary.md)