/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.file.directory.types;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.Nulls;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import core.ObjectMappers;
import java.lang.Object;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import resources.file.types.File;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(
    builder = Directory.Builder.class
)
public final class Directory {
  private final String name;

  private final Optional<List<File>> files;

  private final Optional<List<Directory>> directories;

  private Directory(String name, Optional<List<File>> files,
      Optional<List<Directory>> directories) {
    this.name = name;
    this.files = files;
    this.directories = directories;
  }

  @JsonProperty("name")
  public String getName() {
    return name;
  }

  @JsonProperty("files")
  public Optional<List<File>> getFiles() {
    return files;
  }

  @JsonProperty("directories")
  public Optional<List<Directory>> getDirectories() {
    return directories;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof Directory && equalTo((Directory) other);
  }

  private boolean equalTo(Directory other) {
    return name.equals(other.name) && files.equals(other.files) && directories.equals(other.directories);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.name, this.files, this.directories);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static NameStage builder() {
    return new Builder();
  }

  public interface NameStage {
    _FinalStage name(String name);

    Builder from(Directory other);
  }

  public interface _FinalStage {
    Directory build();

    _FinalStage files(Optional<List<File>> files);

    _FinalStage files(List<File> files);

    _FinalStage directories(Optional<List<Directory>> directories);

    _FinalStage directories(List<Directory> directories);
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder implements NameStage, _FinalStage {
    private String name;

    private Optional<List<Directory>> directories = Optional.empty();

    private Optional<List<File>> files = Optional.empty();

    private Builder() {
    }

    @java.lang.Override
    public Builder from(Directory other) {
      name(other.getName());
      files(other.getFiles());
      directories(other.getDirectories());
      return this;
    }

    @java.lang.Override
    @JsonSetter("name")
    public _FinalStage name(String name) {
      this.name = name;
      return this;
    }

    @java.lang.Override
    public _FinalStage directories(List<Directory> directories) {
      this.directories = Optional.of(directories);
      return this;
    }

    @java.lang.Override
    @JsonSetter(
        value = "directories",
        nulls = Nulls.SKIP
    )
    public _FinalStage directories(Optional<List<Directory>> directories) {
      this.directories = directories;
      return this;
    }

    @java.lang.Override
    public _FinalStage files(List<File> files) {
      this.files = Optional.of(files);
      return this;
    }

    @java.lang.Override
    @JsonSetter(
        value = "files",
        nulls = Nulls.SKIP
    )
    public _FinalStage files(Optional<List<File>> files) {
      this.files = files;
      return this;
    }

    @java.lang.Override
    public Directory build() {
      return new Directory(name, files, directories);
    }
  }
}